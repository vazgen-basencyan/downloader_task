from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .models import Attachment
from .tasks import download_task


class DownloadForm(forms.ModelForm):
    url = forms.CharField(label=' url', max_length=100)

    class Meta:
        model = Attachment
        fields = "url",

    def clean_url(self):
        url = self.cleaned_data['url']
        validate = URLValidator()
        try:
            validate(url)
            return url
        except ValidationError:
            raise forms.ValidationError("Invalid URL")

    def save(self, commit=True):
        attachment = super().save()
        download_task.delay(attachment.id)
        return attachment
