from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth_system.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = 'email', 'password'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class RegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'}))
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'phone'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
