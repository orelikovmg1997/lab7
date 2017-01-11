from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', }),
        min_length=5,
        required=True,
        label='Login'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'First name', }),
        required=True,
        label='Firstname'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Last name', }),
        required=True,
        label='Lastname'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', }),
        required=True,
        label='E-mail'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        min_length=8,
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}),
        min_length=8,
        label=u'Repeat password'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('User with such username already exists')
        except User.DoesNotExist:
            return username

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1', '')
        pass2 = self.cleaned_data.get('password2', '')

        if pass1 != pass2:
            raise forms.ValidationError('Passwords do not match')

    def save(self):
        data = self.cleaned_data
        password = data.get('password1')
        user = User()

        user.username = data.get('username')
        user.password = make_password(password)
        user.email = data.get('email')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.is_active = True
        user.is_superuser = False
        user.save()

        return authenticate(username=user.username, password=password)


class LoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', }
        ),
        max_length=30,
        label='Login'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', }
        ),
        label='Password'
    )

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get('login', ''), password=data.get('password', ''))

        if user is None:
            raise forms.ValidationError('Invalid username or password')
