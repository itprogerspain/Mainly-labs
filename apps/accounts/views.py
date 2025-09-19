from django.contrib.auth.views import LoginView
<<<<<<< HEAD
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
=======
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .forms import (
    CustomLoginForm,
    ProfileForm,
    RegistrationForm,
)



# RegisterView handles new user registration using the custom three-field form
class RegisterView(FormView):
    template_name = "registration/registration_form.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Save the new user instance if the form is valid
        form.save()
        return super().form_valid(form)



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
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
        else:
            return reverse("user_dashboard")


<<<<<<< HEAD
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
=======
# Home page view
def home_view(request):
    return render(request, "home.html")

# Profile edit view (login required)
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "registration/profile_form.html", {"form": form})


# 📊 Admin dashboard view
=======
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        messages.error(request, "Please correct the errors.")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "registration/profile_form.html", {"form": form})

# Dashboards
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")

<<<<<<< HEAD

# 👥 User dashboard view
@login_required
def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")


=======
@login_required
def hr_dashboard(request):
    return render(request, "dashboard/hr_dashboard.html")

@login_required
def tech_dashboard(request):
    return render(request, "dashboard/tech_dashboard.html")

@login_required
def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
