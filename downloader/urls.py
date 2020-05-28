from django.conf.urls import url, include
from downloader import views


urlpatterns = [

    url(r'^export/(?P<id>\d+)/$', views.export_file, name='export_file'),
    url('', views.home, name='home'),
]