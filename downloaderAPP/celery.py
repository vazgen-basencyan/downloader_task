from __future__ import absolute_import, unicode_literals

from celery import Celery


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','downloaderAPP.settings')
app = Celery('downloaderAPP',)

app.autodiscover_tasks()
if __name__ == '__main__':
    app.start()