from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EasySignupForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=50)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Remove the default help texts
            for field in self.fields.values():
                field.help_text = None
                field.widget.attrs['class'] = 'form-control'

