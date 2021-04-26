from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]