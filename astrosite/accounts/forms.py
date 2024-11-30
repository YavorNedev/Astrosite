from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from astrosite.accounts.models import AppUser, Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass


class LogoutForm(AuthenticationForm):
    pass

class profileviewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth']


class ProfileUpdateForm(forms.ModelForm):
   class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }