from django.shortcuts import render, redirect
from app.forms import CadastroForm
from app.forms import DepoimentosForm
from app.forms import EntrarForm
from app.forms import DepoimentosForm
from app.models import CadastroDeUsuario, DepoimentosUsuario
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def mostrar_cadastro(request):
    formulario = CadastroForm(request.POST or None, request.FILES or None)
    menssagem = ''
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            formulario = CadastroForm
            mensagem = 'Cadastro realizado com sucesso'
    contexto = {
        'form' : formulario,
        'mensagem' : menssagem,
    }
    return render(request, 'cadastro.html', contexto)

@csrf_exempt
def mostrar_login(request):
    entrar = EntrarForm(request.POST or None)
    if request.method == 'POST':
        if entrar.is_valid():
            user = request.POST.get('usuario')
            senha = request.POST.get('senha')
            cadastro = CadastroDeUsuario.objects.filter(usuario=user, senha=senha)
            if not cadastro:
                msg='Login ou senha invalido'
                args = {
                    'form': entrar,
                    'msg': msg
                }
                return render(request, 'login.html', args)
            else:
                request.session['usuario'] = user
                return redirect('/painel_usuario')
    return render(request, 'login.html', {'form': entrar})

def mostrar_inicial(request):
    return render(request, 'pagina_inicial.html')

def mostrar_sobre(request):
    return render(request, 'sobre.html')

def mostrar_saiba(request):
    return render(request, 'saiba.html')

@csrf_exempt
def mostrar_painel_usuario(request):
    usuario_x = CadastroDeUsuario.objects.get(usuario = request.session['usuario'])
    depoimentos = DepoimentosForm(request.POST or None, request.FILES or None)
    menssagem = ''
    if request.method == 'POST':
        if depoimentos.is_valid():
            depoimentos.save()
            depoimentos = DepoimentosForm
            mensagem = 'Depoimento enviado com sucesso'
    contexto = {
        'form' : depoimentos,
        'mensagem' : menssagem,
        'usuario_x' : usuario_x,
    }
    return render(request, 'painel_usuario.html', contexto)

def mostrar_comunidade(request):
    depoimentosX = DepoimentosUsuario.objects.all()
    contexto = {
        'depoimentosX' : depoimentosX,
    }
    return render(request, 'comunidade.html', contexto)
