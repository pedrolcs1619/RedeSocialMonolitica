# admin.py

from django.contrib import admin
from .models import Artigo, Comentario, Perfil

# Registrar o modelo Artigo
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('tema', 'autor', 'assunto')  # Exibir os campos no painel
    search_fields = ('tema', 'assunto')  # Adicionar busca por tema e assunto

# Registrar o modelo Comentario
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'usuario', 'comentario')  # Exibir os campos no painel
    search_fields = ('artigo__tema', 'usuario__username')  # Adicionar busca por artigo e usuário

# Registrar o modelo Perfil
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'foto')  # Exibir os campos no painel
    search_fields = ('user__username',)  # Adicionar busca por nome de usuário

# Registrar os modelos no admin
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Perfil, PerfilAdmin)
