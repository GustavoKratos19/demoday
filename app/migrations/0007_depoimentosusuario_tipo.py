# Generated by Django 2.2.3 on 2019-07-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190712_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='depoimentosusuario',
            name='tipo',
            field=models.CharField(choices=[('pu', 'Público'), ('pv', 'Privado')], default='', max_length=2),
        ),
    ]