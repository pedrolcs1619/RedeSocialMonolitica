from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    imagem = models.ImageField(upload_to='capas/')

    def __str__(self):
        return self.titulo
