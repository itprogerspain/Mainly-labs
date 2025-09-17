from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import (
    CustomLoginForm,
    ProfileForm,
)

# Custom login view with role-based redirect
class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginForm

    def get_success_url(self):
        user = self.request.user

        if user.role == "admin":
            return reverse("admin_dashboard")
        elif user.role == "hr":
            return reverse("hr_dashboard")
        elif user.role == "tech":
            return reverse("tech_dashboard")
        else:
            return reverse("user_dashboard")


# Home page view
def home_view(request):
    return render(request, "home.html")

# Profile edit view (login required)
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        messages.error(request, "Please correct the errors.")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "registration/profile_form.html", {"form": form})

# Dashboards
@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")

@login_required
def hr_dashboard(request):
    return render(request, "dashboard/hr_dashboard.html")

@login_required
def tech_dashboard(request):
    return render(request, "dashboard/tech_dashboard.html")

@login_required
def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")
