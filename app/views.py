from django.shortcuts import render
from app.froms import CadastroForm
from app.froms import DepoimentosForm

# Create your views here.

def mostrar_layout(request):
    return render(request, 'layout.html')

def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None)
    menssagem = ''
    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm
        menssagem = 'Cadastro realizado com sucesso'
    contexto = {
        'form' : formulario,
        'menssagem' : menssagem,
    }
    return render(request, 'cadastro.html', contexto)

def mostrar_login(request):
    return render(request, 'login.html')

def mostrar_inicial(request):
    return render(request, 'pagina_inicial.html')

def mostrar_comunidade(request):
    return render(request, 'comunidade.html')

