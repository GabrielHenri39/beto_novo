from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.messages import constants
from .utils import password_is_valid
from .models import User
from rest_framework import status


def login(request):
    """
    Realiza o login de um usuário no sistema.
    :param request: HttpRequest
    :return: HttpResponseRedirect
    """

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=password)

        if not usuario:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos.')
            return redirect('/auth/login', status=status.HTTP_302_FOUND)
        else:
            auth.login(request, usuario)
            return redirect('/')
    return redirect(reverse('login'), status=status.HTTP_302_FOUND)


def cadastro(request):
    """
    Cadastra um novo usuário no sistema.
    :param request: HttpRequest
    :return: HttpResponseRedirect
    """

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')

        if not password_is_valid(request, password, check_password):
            return redirect(reverse('cadastro'))

        user, create = User.objects.get_or_create(
            username=user_name, email=email, password=password)
        if not create:
            messages.add_message(
                request, constants.ERROR, 'Já existe um usuário com esse e-mail ou usuário')
            return redirect(reverse('cadastro'))
        return redirect(reverse('login'))


def sair(request):
    """
    Realiza o logout de um usuário no sistema.
    :param request: HttpRequest
    :return: HttpResponseRedirect
    """
    if not request.user.is_authenticated:

        return redirect(reverse('login'))

    auth.logout(request)
    return redirect(reverse('login'))
