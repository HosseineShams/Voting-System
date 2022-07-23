from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    # student_number = forms.IntegerField()
    # identity_number = forms.IntegerField()
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']
        widgets = {
            'password': forms.PasswordInput,
        }

class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


