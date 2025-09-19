from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import (
    CustomPasswordResetForm,
<<<<<<< HEAD
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
=======
    CustomPasswordChangeForm,
)

urlpatterns = [
    # Login / Logout
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Home
    path("home/", views.home_view, name="home"),

    # Profile
    path("profile/", views.profile, name="profile"),

    # Registration
    path("register/", views.RegisterView.as_view(), name="register"),

    # Password reset (request email)
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        form_class=CustomPasswordResetForm
    ), name="password_reset"),

<<<<<<< HEAD

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

=======
    # Password change
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change_form.html",
        form_class=CustomPasswordChangeForm
    ), name="password_change"),
<<<<<<< HEAD

    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"
    ), name="password_change_done"),
]
=======
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/password_change_done.html"
    ), name="password_change_done"),

    # Dashboards by role
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/hr/", views.hr_dashboard, name="hr_dashboard"),
    path("dashboard/tech/", views.tech_dashboard, name="tech_dashboard"),
    path("dashboard/user/", views.user_dashboard, name="user_dashboard"),
]

>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
