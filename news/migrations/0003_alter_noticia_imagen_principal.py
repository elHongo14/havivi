# Generated by Django 5.1.6 on 2025-03-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_noticia_imagen_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen_principal',
            field=models.ImageField(blank=True, default='media/dummy_img.jpg', help_text='El tamaño de la imagen deberá ser menor a 2MB', null=True, upload_to='media/noticias'),
        ),
    ]
