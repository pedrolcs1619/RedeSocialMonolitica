from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    # Campos padrão
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Senha")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmação de Senha")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Email")
    
    # Adicionando o campo para selecionar entre 'user' e 'funcionário'
    ROLE_CHOICES = [
        ('user', 'User'),
        ('funcionario', 'Funcionário'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Tipo de Usuário", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']  # Campos que aparecerão no formulário

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    # Salvando o usuário
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Criptografa a senha
        if commit:
            user.save()  # Salva o usuário
        return user

