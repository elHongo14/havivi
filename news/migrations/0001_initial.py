# Generated by Django 5.1.6 on 2025-03-02 01:10

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Tipo de Noticia',
                'verbose_name_plural': 'Tipos de Noticia',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=200)),
                ('cuerpo_noticia', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Cuerpo Noticia')),
                ('imagen_principal', models.ImageField(blank=True, default='dummy_img.jpg', help_text='El tamaño de la imagen deberá ser menor a 2MB', null=True, upload_to='noticias')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_noticia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.tipo_noticia')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
