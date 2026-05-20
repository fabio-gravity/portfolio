from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistoForm
import uuid


# === LOGIN ===

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio:index')
        else:
            messages.error(request, 'Username ou password incorretos.')
    return render(request, 'accounts/login.html')


# === LOGOUT ===

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


# === REGISTO ===

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adicionar ao grupo autores automaticamente
            grupo, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            login(request, user)
            return redirect('portfolio:index')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})


# === MAGIC LINK ===

magic_tokens = {}

def magic_link_request_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = str(uuid.uuid4())
            magic_tokens[token] = user.id

            link = request.build_absolute_uri(f'/accounts/magic-login/{token}/')
            send_mail(
                'O seu link de acesso',
                f'Clique no link para aceder: {link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )
            messages.success(request, 'Link enviado para o seu email!')
        except User.DoesNotExist:
            messages.error(request, 'Email não encontrado.')
    return render(request, 'accounts/magic_link.html')


def magic_link_login_view(request, token):
    user_id = magic_tokens.pop(token, None)
    if user_id:
        user = User.objects.get(id=user_id)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('portfolio:index')
    else:
        messages.error(request, 'Link inválido ou expirado.')
        return redirect('accounts:login')
