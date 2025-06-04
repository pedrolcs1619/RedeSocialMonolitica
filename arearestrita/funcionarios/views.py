from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):
    return render(request, 'funcionarios/home.html')

@login_required
def painel(request):
    return render(request, 'funcionarios/painel.html')

@login_required
def perfil(request):
    return render(request, 'funcionarios/perfil.html', {'usuario': request.user})

class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')
    
def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Cria o usuário
            login(request, user)  # Faz login automático após o cadastro
            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'funcionarios/cadastro.html', {'form': form})
    

    

