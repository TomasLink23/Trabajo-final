# Generated by Django 4.0.4 on 2022-06-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil_usuario_imagen_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil_usuario',
            old_name='Region',
            new_name='region',
        ),
        migrations.AlterField(
            model_name='perfil_usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
