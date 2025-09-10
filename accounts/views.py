from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

def home_view(request):
    return render(request, 'home.html')

