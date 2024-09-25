

from django import forms
from .models import StudentRegistration, StudentFees

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'signature': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'languages': forms.CheckboxSelectMultiple(),
         
        }


class StudentFeesform(forms.ModelForm):
    class Meta:
        model = StudentFees
        fields = ['mobile_number']
        widgets = {'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),}


