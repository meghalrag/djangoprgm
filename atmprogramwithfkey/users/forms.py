from django import forms  
from users.models import * 
class Profileform(forms.Form):  
    picname=forms.ImageField()