# Generated by Django 5.0.6 on 2024-06-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_perfilusuario_usuario_perfilusuario_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
