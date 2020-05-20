from django.db import models


class Attachment(models.Model):
    file = models.FileField(verbose_name="file")
    url = models.CharField(max_length=1024)
    status = models.CharField(max_length=64)