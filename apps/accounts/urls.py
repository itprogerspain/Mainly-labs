from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import (
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    CustomPasswordChangeForm
)

urlpatterns = [
    # 🔑 Login / Logout
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # 🏠
    path("home/", views.home_view, name="home"),

    # 📝 Registro
    path("register/", views.register, name="register"),

    # 👤 Perfil
    path("profile/", views.profile, name="profile"),

    # 🔄 Reset password
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        form_class=CustomPasswordResetForm
    ), name="password_reset"),


    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html",
        form_class=CustomSetPasswordForm
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ), name="password_reset_complete"),

    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change_form.html",
        form_class=CustomPasswordChangeForm
    ), name="password_change"),

    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"
    ), name="password_change_done"),
]
