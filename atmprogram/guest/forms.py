from django import forms  
from users.models import Atmdb  
  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Atmdb  
        fields = ('username','password') 