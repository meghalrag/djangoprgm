from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/',indexpage,name='index'),
    url(r'register/',registration,name='register'),
    url(r'login/',login,name='login'),
    url(r'formreg',formreg,name='formreg'),
    url(r'formlogin',formlogin,name='formlogin'),

]