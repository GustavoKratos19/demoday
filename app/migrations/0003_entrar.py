# Generated by Django 2.2.3 on 2019-07-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190708_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='', max_length=40)),
                ('senha', models.CharField(default='', max_length=23)),
            ],
        ),
    ]
