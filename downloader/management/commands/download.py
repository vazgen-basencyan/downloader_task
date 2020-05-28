from django.core.management.base import BaseCommand, CommandError
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from downloader.models import Attachment
from downloader.tasks import download_task


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options.get("url")
        if not url:
            self.stdout.write("No specified url for download")
        validate = URLValidator()
        attachment = Attachment.objects.create(url=url)
        self.stdout.write("Downloading from {}".format(url))
        download_task.delay(attachment.id)
        self.stdout.write("Download complete")

        try:
            validate(url)
        except ValidationError:
            self.stdout.write("invalid url {}".format(url))
