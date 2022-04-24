from django import forms
from django.forms import ModelForm
from .models import DonorList
    

class DonorRegistration(ModelForm):
    class Meta:
        model = DonorList
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'last_donate_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            
        }
        

