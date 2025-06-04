from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Página pública
    path('painel/', views.painel, name='painel'),  # Painel restrito
    path('perfil/', views.perfil, name='perfil'),  # Página de perfil

    # Login, Logout e cadastro
    path('login/', auth_views.LoginView.as_view(template_name='funcionarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),  # URL para o cadastro
    
]

