from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscrap-home'),
    path('Login/', views.login, name='subscrap-login'),
    path('Signup/', views.signup, name='subscrap-signup'),
    
]
