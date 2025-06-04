"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py (principal)
from django.contrib import admin
from django.urls import path, include  # 'include' permite incluir as URLs do seu app
from app import views  # ou o nome do seu app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin do Django
    path('', include('app.urls')),  # Inclua as URLs do seu app (substitua 'seu_app' pelo nome real do seu app)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
] 
