# Generated by Django 4.2.7 on 2023-12-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_perfil_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(default='users/imagenes/users.jpg', upload_to='users/imagenes'),
        ),
    ]
