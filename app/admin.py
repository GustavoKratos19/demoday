from django.contrib import admin
from app.models import CadastroDeUsuario
from app.models import DepoimentosUsuario

# Register your models here.

admin.site.register(CadastroDeUsuario)
admin.site.register(DepoimentosUsuario)