from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView,ListView
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'get/',getfunc,name='get'),
    url(r'home/',indexpage,name='home'),
    # url(r'display/',display,name='display'),
    url(r'display/',display,name='display'),
    url(r'profileupdate/',TemplateView.as_view(template_name = 'updatepro.html'),name='profileupdate'),
    url(r'updateform/',updateform,name='updateform'),
    url(r'listview/', ListView.as_view(model = Atmdb, 
      template_name = "ajaxsample.html")),
    url(r'logout/',logout,name='logout'),
    url(r'getajax/',getajax,name='getajax'),
    url(r'mmm/',myname,name='mmm'),
]