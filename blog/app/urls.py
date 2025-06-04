from django.urls import path  # Importa a função 'path' para definir as URLs
from . import views  # Importa as views do aplicativo atual
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django
from django.conf import settings  # Importa as configurações do projeto
from django.conf.urls.static import static  # Importa para servir arquivos estáticos durante o desenvolvimento
from django.contrib.auth.decorators import login_required  # Importa o decorador para garantir que a página seja acessada por usuários autenticados


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('criar/', login_required(views.criar_artigo), name='criar_artigo'),
    path('artigos/', login_required(views.lista_artigos), name='lista_artigos'),
    path('artigo/editar/<int:pk>/', login_required(views.editar_artigo), name='editar_artigo'),
    path('artigo/excluir/<int:pk>/', login_required(views.excluir_artigo), name='excluir_artigo'),
    path('artigo/<int:pk>/comentar/', login_required(views.comentar_artigo), name='comentar_artigo'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('entrar-como-visitante/', views.entrar_como_visitante, name='entrar_como_visitante'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
