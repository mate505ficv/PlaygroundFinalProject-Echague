# Generated by Django 4.2.3 on 2023-08-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPaggina', '0002_curso_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(upload_to='tareas/')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
