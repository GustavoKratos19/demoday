from django.db import models

# Create your models here.
class CadastroDeUsuario(models.Model):
    genero_opcoes = [
        ('fem', 'Feminino'),
        ('tra', 'Transsexual'),
        ('otr', 'Outros')
    ]

    nome_usuario = models.CharField(max_length=100)
    email_usuario = models.EmailField(max_length=254)
    usuario = models.CharField(max_length=20)
    data_nacimento_usuario = models.CharField(max_length=10)
    cpf_usuario = models.CharField(max_length=14)
    celular_usuario = models.CharField(max_length=14)
    genero_usuario = models.CharField(max_length=3, choices=genero_opcoes)
    senha_usuario = models.CharField(max_length=30)
    foto_usuario = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome_usuario

class DepoimentosUsuario(models.Model):
    titulo_depoimento = models.CharField(max_length=40)
    depoimento = models.TextField(default='')
    foto_depoimento = models.ImageField(upload_to='')
    nome_usuario = models.ForeignKey(CadastroDeUsuario, on_delete=models.SET_DEFAULT, default='')

    def __str__(self):
        return self.titulo_depoimento