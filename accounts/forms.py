from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm
)

CustomUser = get_user_model()


# 🔑 Login
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


# 📝 Registro
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la contraseña',
            'class': 'form-control'
        })
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


# 🔄 Recuperar contraseña (envío email)
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })
    )


# 🔐 Nueva contraseña (после перехода по ссылке)
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nueva contraseña',
            'class': 'form-control'
        })
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la nueva contraseña',
            'class': 'form-control'
        })
    )


# 🔏 Cambiar contraseña (когда пользователь залогинен)
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña actual',
            'class': 'form-control'
        })
    )
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nueva contraseña',
            'class': 'form-control'
        })
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la nueva contraseña',
            'class': 'form-control'
        })
    )


# 👤 Editar perfil
class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })
    )
    avatar = forms.ImageField(
        label="Avatar",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ("username", "email")

