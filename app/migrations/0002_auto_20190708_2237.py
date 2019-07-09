# Generated by Django 2.2.3 on 2019-07-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='celular',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='cpf',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='data_nascimento',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='genero',
            field=models.CharField(choices=[('fem', 'Feminino'), ('mas', 'Masculino'), ('otr', 'Outros')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='senha',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='cadastrodeusuario',
            name='usuario',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='depoimentosusuario',
            name='titulo_depoimento',
            field=models.CharField(default='', max_length=40),
        ),
    ]
