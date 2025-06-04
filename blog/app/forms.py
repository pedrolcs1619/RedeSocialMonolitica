# forms.py
from django import forms
from .models import Artigo
from django import forms
from .models import Comentario

from django import forms
from .models import Perfil



class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['tema', 'assunto']
        widgets = {
            'tema': forms.TextInput(attrs={
                'class': 'form-control rounded-input',  # Adiciona uma classe CSS para bordas arredondadas
                'placeholder': 'Digite o tema do artigo',  # Adiciona um texto de exemplo
            }),
            'assunto': forms.Textarea(attrs={
                'class': 'form-control rounded-input',  # Adiciona uma classe CSS para bordas arredondadas
                'placeholder': 'Descreva o assunto do artigo',  # Adiciona um texto de exemplo
                'rows': 5,  # Define a altura do campo de "assunto"
            }),
        }





from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'class': 'form-control',  # Adiciona a classe para estilizar o campo
                'placeholder': 'Digite seu comentário...',  # Texto de exemplo dentro da caixa
                'style': 'border-radius: 25px;height: 50px;',  # Estilo adicional, caso queira
            })
        }




class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
