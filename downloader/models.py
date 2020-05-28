from django.db import models


class Attachment(models.Model):
    FAILED = 0
    PENDING = 1
    DONE = 2
    STATUS_CHOICES = (
        (FAILED, 'Failed'),
        (PENDING, 'Pending'),
        (DONE, 'Done'),
    )
    file = models.FileField(verbose_name="file")
    url = models.SlugField(max_length=1024)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)


