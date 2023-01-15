from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'id' : 'usename',
            'type' : 'text',
            'class' : 'form-input',
            'placeholder' : 'Fariz',
            'maxlength': '16',
            'minlength' : '6',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'Fariz@gmail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'password1',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'password2',
            'maxlength': '16',
            'minlength': '6',
        })


    class Meta:
        model = User
        fields = ['username','email','password1','password2']