from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import (
    CustomLoginForm,
    CustomUserCreationForm,
    ProfileForm,
)

# 🔑 Кастомная вьюшка логина
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


# 🏠 Домашняя страница
def home_view(request):
    return render(request, "home.html")


# 📝 Регистрация
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # сразу авторизуем пользователя
            messages.success(request, "¡Registro completado con éxito!")
            return redirect("home")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/registration_form.html", {"form": form})


# 👤 Редактирование профиля (требует входа)
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


