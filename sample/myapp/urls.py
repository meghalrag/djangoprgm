from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'hello',show,name='hello'),
    url(r'html',htmlshow,name='html'),
    url(r'ffff',html2show,name='html2'),
    url(r'formh',insertdb,name='formh'),
    url(r'startdb',dbshow,name='startdb'),
    url(r'update',dbupdate,name='update'),
    url(r'delete',dbdelete,name='delete'),
    url(r'getf',dbget,name='getf')
]
