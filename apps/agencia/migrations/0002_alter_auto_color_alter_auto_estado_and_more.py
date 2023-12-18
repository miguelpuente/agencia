# Generated by Django 4.2.7 on 2023-12-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='color',
            field=models.CharField(choices=[('BLA', 'BLANCO'), ('NEG', 'NEGRO'), ('ROJ', 'ROJO')], default='BLA', max_length=3),
        ),
        migrations.AlterField(
            model_name='auto',
            name='estado',
            field=models.CharField(choices=[('D', 'DISPONIBLE'), ('R', 'RESERVADO'), ('V', 'VENDIDO')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='auto',
            name='transmision',
            field=models.CharField(choices=[('A', 'AUTOMÁTICA'), ('M', 'MANUAL')], default='M', max_length=3),
        ),
    ]
