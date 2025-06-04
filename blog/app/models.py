# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Artigo(models.Model):
    tema = models.CharField(max_length=100)
    assunto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(default=timezone.now)  # Defina um valor padrão com timezone.now()
    #TO-DO: imagem = models.ImageField(upload_to='artigos/', blank=True, null=True)  

    def __str__(self):
        return self.tema

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.artigo.tema}"


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)

    def __str__(self):
        return self.user.username


