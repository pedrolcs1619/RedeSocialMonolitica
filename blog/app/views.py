from .models import Perfil
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm
from django.shortcuts import render, redirect
from .forms import PerfilForm



# View para a página de criação de artigo (criar.html)
@login_required
def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm()

    return render(request, 'artigos/criar.html', {'form': form})


# View para a página de lista de artigos (lista.html)
def lista_artigos(request):
    q = request.GET.get('q', '')
    order = request.GET.get('order', 'desc')

    artigos = Artigo.objects.all()

    if q:
        artigos = artigos.filter(
            Q(tema__icontains=q) |
            Q(autor__username__icontains=q)
        )

    artigos = artigos.order_by('criado_em')

    paginator = Paginator(artigos, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'artigos/lista.html', {
        'artigos': page_obj,
        'q': q,
        'order': order,
    })


# View para editar um artigo existente (editar.html)
def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm(instance=artigo)
    
    return render(request, 'artigos/editar_artigo.html', {
        'form': form,
        'artigo': artigo
    })


# View para excluir um artigo (excluir.html)
def excluir_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.method == 'POST':
        artigo.delete()
        return redirect('lista_artigos')
    
    return render(request, 'artigos/excluir_artigo.html', {'artigo': artigo})


# Cadastro de usuário (cadastro.html)
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados e tente novamente.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/cadastro.html', {'form': form})


# Logout de usuário (logout.html)
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


# View para adicionar um comentário em um artigo (comentar_artigo.html)
@login_required
def comentar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.usuario = request.user
            comentario.save()
            return redirect('comentar_artigo', pk=artigo.pk)
    else:
        form = ComentarioForm()

    comentarios = artigo.comentarios.all()

    return render(request, 'artigos/comentar_artigo.html', {
        'artigo': artigo,
        'form': form,
        'comentarios': comentarios
    })


# View para editar perfil do usuário (editar_perfil.html)
@login_required
def editar_perfil(request):
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')
    else:
        form = PerfilForm(instance=perfil)

    artigos = Artigo.objects.filter(autor=request.user)

    return render(request, 'perfil/editar_perfil.html', {'form': form, 'perfil': perfil, 'artigos': artigos})


# View para entrar como visitante e ver todos os artigos
def entrar_como_visitante(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/lista.html', {'artigos': artigos})
