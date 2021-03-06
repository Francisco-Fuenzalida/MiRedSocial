from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def inicio(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'inicio.html', data)

def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    data = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'perfil.html', data)

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()
    data = {
        'form': form
    }
    return render(request, 'registro.html', data)

def publicar(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Has hecho una publicación')
            return redirect('inicio')
    else:
        form = PostForm()
    data = {
        'form': form
    }
    return render(request, 'publicar.html', data)

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Siguiendo a {username}')
    return redirect('inicio')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('inicio')
    