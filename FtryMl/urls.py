from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from .common import r404
from .pages import uploadImg
 
urlpatterns = [
    url(r'^upload_file$', uploadImg.upload_file),
    url(r'^admin/', admin.site.urls),
    url(r'^$', r404.result),
]