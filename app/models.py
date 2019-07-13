from django.db import models

# Create your models here.
class CadastroDeUsuario(models.Model):
    genero_opcoes = [
        ('', ''),
        ('fem', 'Feminino'),
        ('otr', 'Outros'),
    ]

    nome = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=254, default='')
    usuario = models.CharField(max_length=20, default='')
    data_nascimento = models.CharField(max_length=10, default='')
    cpf = models.CharField(max_length=14, default='')
    celular = models.CharField(max_length=14, default='')
    genero = models.CharField(max_length=3, choices=genero_opcoes, default='')
    senha = models.CharField(max_length=30, default='')
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome

class DepoimentosUsuario(models.Model):
    tipo_depoimento = [
        ('', ''),
        ('pu', 'Público'),
        ('pv', 'Privado'),
    ]

    titulo_depoimento = models.CharField(max_length=40, default='')
    depoimento = models.TextField(default='')
    imagem = models.ImageField(upload_to='')
    tipo = models.CharField(max_length=2, choices=tipo_depoimento, default='')
    nome = models.ForeignKey(CadastroDeUsuario, on_delete=models.SET_DEFAULT, default='')

    def __str__(self):
        return self.titulo_depoimento
