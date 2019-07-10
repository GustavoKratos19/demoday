from django.shortcuts import render
from app.forms import CadastroForm
from app.forms import DepoimentosForm

# Create your views here.


def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None, request.FILES or None)
    menssagem = ''
    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm
        mensagem = 'Cadastro realizado com sucesso'
    contexto = {
        'form' : formulario,
        'mensagem' : menssagem,
    }
    return render(request, 'cadastro.html', contexto)

def mostrar_login(request):
    return render(request, 'login.html')

def mostrar_inicial(request):
    return render(request, 'pagina_inicial.html')

def mostrar_comunidade(request):
    return render(request, 'comunidade.html')

def mostrar_sobre(request):
    return render(request, 'sobre.html')

