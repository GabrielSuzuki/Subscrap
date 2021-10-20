from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='subscrap-home'),
    path('Login/', views.login, name='subscrap-login'),
    path('Signup/', views.signup, name='subscrap-signup'),
    
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)