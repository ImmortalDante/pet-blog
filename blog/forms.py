# def cleaned_title(self): --> simple example of custom form validation
#     title = self.cleaned_data["title"]
#     if something:
#         raise ValidationError("Text")
#     return title
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
