# Generated by Django 2.2.3 on 2019-07-06 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='celular_usuario',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='cpf_usuario',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='data_nacimento_usuario',
            new_name='data_nacimento',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='email_usuario',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='foto_usuario',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='genero_usuario',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='nome_usuario',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='cadastrodeusuario',
            old_name='senha_usuario',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='depoimentosusuario',
            old_name='nome_usuario',
            new_name='nome',
        ),
    ]