from django.shortcuts import render
from app.froms import CadastroForm
from app.froms import DepoimentosForm

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None)
    menssagem = ''
    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm
        menssagem = 'Cadastro realizado com sucesso'
    return render(request, 'cadastro.html')