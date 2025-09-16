from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse

from .forms import (
    CustomLoginForm,
    CustomUserCreationForm,
    ProfileForm,
)

# 🔑 Custom login view with role-based redirect
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        user = self.request.user
        # redirect based on user role
        if user.role == "admin":
            return reverse("admin_dashboard")
        else:
            return reverse("user_dashboard")


# 🏠 Home page
def home_view(request):
    return render(request, "home.html")


# 📝 Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in user immediately
            messages.success(request, "¡Registro completado con éxito!")
            # redirect based on role
            if user.role == "admin":
                return redirect("admin_dashboard")
            else:
                return redirect("user_dashboard")
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/registration_form.html", {"form": form})


# 👤 Editing profile (login required)
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "registration/profile_form.html", {"form": form})


# 📊 Admin dashboard view
@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")


# 👥 User dashboard view
@login_required
def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")