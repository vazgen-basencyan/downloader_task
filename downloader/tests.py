from django.test import Client, TestCase
from django.test import  TestCase


from .models import Attachment
from .tasks import download_task

class TestDownloadFlow(TestCase):
    FILE_URL = 'https://stackoverflow.com/questions/57981659/django-2-2-5-url-regex-in-url-path'

    def test_home_page(self):
        client = Client()
        res = client.post('', data={"url": TestDownloadFlow.FILE_URL})
        self.assertEqual(res.status_code, 200)

    def test_download_task(self):
        download_task(url=TestDownloadFlow.FILE_URL)
        self.assertEqual(Attachment.objects.count(), 1)





