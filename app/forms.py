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
        widgets = {
            'senha': forms.PasswordInput(),
        }

class DepoimentosForm(forms.ModelForm):
    class Meta:
        model = DepoimentosUsuario
        fields = [
            'titulo_depoimento',
            'depoimento',
            'imagem',
            'tipo',
        ]

class EntrarForm(forms.Form):
    usuario = forms.CharField(max_length=40)
    senha = forms.CharField(max_length=23, widget= forms.PasswordInput)