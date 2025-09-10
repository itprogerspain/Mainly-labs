from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
