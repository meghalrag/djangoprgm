from django import forms  
from users.models import * 
class loginform(forms.ModelForm):  
    class Meta:  
        model = logintable
        fields = ('username','password')
class regform(forms.ModelForm):  
    class Meta:  
        model = registertable
        fields = ('emailid',)
