from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView,ListView
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home/',indexpage,name='home'),
    # url(r'display/',display,name='display'),
    url(r'display/',display,name='display'),
    url(r'profileupdate/',TemplateView.as_view(template_name = 'updatepro.html'),name='profileupdate'),
    url(r'updateform/',updateform,name='updateform'),
    url(r'picupdate/',TemplateView.as_view(template_name = 'propic.html'),name='picupdate'),
    url(r'updatepic/',profileadd,name='updatepic'),
    url(r'logout/',logout,name='logout'),
]