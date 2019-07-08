from django import forms
from app.models import CadastroDeUsuario
from app.models import DepoimentosUsuario

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

class DepoimentosForm(forms.ModelForm):
    class Meta:
        model = DepoimentosUsuario
        fields = [
            'titulo_depoimento',
            'depoimento',
            'foto_depoimento',
        ]