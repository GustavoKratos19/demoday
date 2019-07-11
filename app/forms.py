from django import forms
from app.models import CadastroDeUsuario
from app.models import DepoimentosUsuario
from app.models import Entrar

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroDeUsuario
        fields = [
            'nome',
            'email',
            'usuario',
            'data_nascimento',
            'cpf',
            'celular',
            'genero',
            'senha',
            'foto',
        ]
        widgets = {
            'senha': forms.PasswordInput(),
        }

class DepoimentosForm(forms.ModelForm):
    class Meta:
        model = DepoimentosUsuario
        fields = [
            'titulo_depoimento',
            'depoimento',
            'foto_depoimento',
        ]

class EntraForm(forms.ModelForm):
    class Meta:
        model = Entrar
        fields = [
            'usuario',
            'email',
            'senha',
        ]
        widgets = {
            'senha': forms.PasswordInput(),
        }