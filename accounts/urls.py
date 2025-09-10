# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     ...
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]