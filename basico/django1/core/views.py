from django.shortcuts import render

# Create your views here.
def index(request):
    print(dir(request.user))
    print(f'User: {request.user}')

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario Não Logado'
    else:
        teste = 'Usuario Logado'

    context = {
        'curso': 'Programação WEB com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
