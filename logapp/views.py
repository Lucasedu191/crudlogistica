from django.shortcuts import render
from .models import Agendar, Caracterisca, Cliente

def index(request):
    agendar = Agendar.objects.all()
    caracteristicas = Caracterisca.objects.all()

    context = {
        'frota': 'Frota de veículos',
        'agendar': agendar,
        'caracteristicas': caracteristicas,
        'cliente': cliente,
    }
    return render(request, 'index.html', context)

def agenda(request):
    agendar = Agendar.objects.all()
    context = {

        'agendar': agendar,
    }
    return render(request, 'agendar.html', context)

def cliente(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'clientes.html', context)

def caracteristica(request):
    caracteristicas = Caracterisca.objects.all()
    context = {
        'caracteristicas': caracteristicas,
    }
    return render(request, 'caracteristica.html', context)
