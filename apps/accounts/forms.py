from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)
from django.contrib.auth.password_validation import password_validators_help_text_html

# Get custom user model
CustomUser = get_user_model()


# Login form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control',
            'autocomplete': 'current-password'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


# Registration form
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control',
            'autocomplete': 'email'
        })
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


# Password reset (request email)
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control',
            'autocomplete': 'email'
        })
    )


# Set new password (after visiting reset link)
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nueva contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la nueva contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )


# Change password (user is logged in)
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña actual',
            'class': 'form-control',
            'autocomplete': 'current-password'
        })
    )
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Nueva contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite la nueva contraseña',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
    )


# Profile edit form
class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control',
            'autocomplete': 'email'
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

