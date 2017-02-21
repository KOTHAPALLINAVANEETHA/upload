
from django import forms
from .models import Personal
from .models import Official
from .models import Leave,Upload
from django import forms
#from uploads.core.models import Document
from .models import Upload
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.extras.widgets import SelectDateWidget
from .models import *



class PersonalForm(forms.ModelForm):
    DOB = forms.DateField(label='date of birth',widget = SelectDateWidget(years = range(2020, 1970, -1)))
    bloodgroup = forms.ChoiceField(choices=BLOODGROUPS,required=True)
    marital_status = forms.ChoiceField(choices=MARITALSTATUS,required=True)
    
    class Meta:
    	model = Personal
    	fields ='__all__'

class OfficialForm(forms.ModelForm):
    Designations = forms.ChoiceField(choices=DESIGNATIONS,required=True)
    DOJ = forms.DateField(label='date of joining',widget= SelectDateWidget)
    Departments = forms.ChoiceField(choices=DEPARTMENTS,required=True)
    codes = forms.ChoiceField(choices=CODES,required=True)


    class Meta:
        model = Official
        fields ='__all__'
'''
class DepartmentForm(forms.ModelForm):
	Departments = forms.ChoiceField(choices=DEPARTMENTS,required=True)
    codes = forms.ChoiceField(choices=CODES,required=True)


	class Meta:
		model = Department

class LeaveForm(forms.ModelForm):
    leaves = forms.ChoiceField(choices=LEAVES, required=True)
    leaves_taken = forms.DateField(label='no of leaves taken',widget=SelectDateWidget(required=False))

    class Meta:
		model = Leave
'''

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username','required':'required'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password','required':'required'}))

class UploadForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = '__all__'