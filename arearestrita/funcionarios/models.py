from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('funcionario', 'Funcionário'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
