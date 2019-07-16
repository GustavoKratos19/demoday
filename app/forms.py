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
        widgets = {
            'titulo_depoimento': forms.TextInput(attrs={'placeholder': 'De um titulo ao seu depoimento'}),
            'depoimento': forms.Textarea(attrs={'placeholder': 'Digite aqui o seu depoimento ..........'}),
        }      

class EntrarForm(forms.Form):
    usuario = forms.CharField(max_length=40, widget= forms.TextInput(attrs={'placeholder': 'Digite seu Usuario'}))
    senha = forms.CharField(max_length=23, widget= forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))