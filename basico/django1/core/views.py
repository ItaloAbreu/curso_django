from django.shortcuts import render

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação WEB com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(pk=pk)
    print(prod)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
