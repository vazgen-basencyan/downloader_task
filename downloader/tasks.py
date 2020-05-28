import requests

from django.core.files.base import ContentFile
from celery import shared_task

from downloader.models import Attachment


@shared_task
def download_task(attachment_id):
    attachment = Attachment.objects.get(id=attachment_id)
    url = attachment.url
    try:
        split_link = url.split('/')
        file_name = split_link[-1:][0]
        res = requests.get(url)

        file = ContentFile(res.content)
        file.name = file_name

        attachment.file = file
        attachment.status = Attachment.DONE
    except:
        attachment.status = Attachment.FAILED
    attachment.save()