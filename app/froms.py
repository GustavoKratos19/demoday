from django import forms
from app.models import CadastroDeUsuario
from app.models import DepoimentosUsuario

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroDeUsuario
        fields = [
            'nome_usuario',
            'email_usuario',
            'usuario',
            'data_nacimento_usuario',
            'cpf_usuario',
            'celular_usuario',
            'genero_usuario',
            'senha_usuario',
            'foto_usuario',
        ]

class DepoimentosForm(forms.ModelForm):
    class Meta:
        model = DepoimentosUsuario
        fields = [
            'titulo_depoimento',
            'depoimento',
            'foto_depoimento',
        ]