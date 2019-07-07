from django.db import models

# Create your models here.
class CadastroDeUsuario(models.Model):
    genero_opcoes = [
        ('fem', 'Feminino'),
        ('tra', 'Transsexual'),
        ('otr', 'Outros')
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    usuario = models.CharField(max_length=20)
    data_nascimento = models.CharField(max_length=10)
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=14)
    genero = models.CharField(max_length=3, choices=genero_opcoes)
    senha = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome_usuario

class DepoimentosUsuario(models.Model):
    titulo_depoimento = models.CharField(max_length=40)
    depoimento = models.TextField(default='')
    foto_depoimento = models.ImageField(upload_to='')
    nome = models.ForeignKey(CadastroDeUsuario, on_delete=models.SET_DEFAULT, default='')

    def __str__(self):
        return self.titulo_depoimento