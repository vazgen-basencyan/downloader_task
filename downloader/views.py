from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from downloader.tasks import download_task
from .forms import DownloadForm
from .models import Attachment

@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            form.save()
    form = DownloadForm()
    attachments = Attachment.objects.all()
    return render(request, 'downloader/home.html', {'form': form, 'attachments': attachments},)


def export_file(request, id):
    attachment = Attachment.objects.get(id=str(id))
    response = FileResponse(attachment.file.file.file)
    response['Content-Disposition'] = 'attachment; filename={}'.format(attachment.file)
    return response
