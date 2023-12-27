from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ClienteForm
from .models import Cliente
from django.contrib import messages
from django.contrib.messages import constants
@login_required(login_url='auth/login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='auth/login')
def cadastra_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome'].strip()
            telefone = form.cleaned_data['telefone'].strip()

            if not nome:
                messages.add_message(request,constants.ERROR, 'O nome não pode ser vazio.')
            elif not telefone:
                messages.add_message( request, constants.ERROR, 'O telefone não pode ser vazio.')
            else:
                cliente, created = Cliente.objects.get_or_create(
                    nome=nome,
                    telefone=telefone
                )
                if created:
                    messages.add_message(request, constants.SUCCESS,'Cliente cadastrado com sucesso.')
                else:
                    messages.add_message( request,constants.ERROR,'Jáexiste um cliente com esse nome.')
                return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'cadastra_cliente.html', {'form': form})























