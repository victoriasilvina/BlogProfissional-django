# Generated by Django 5.1.1 on 2024-09-20 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoal',
            old_name='subtitulo',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='pessoal',
            old_name='titulo',
            new_name='parentesco',
        ),
    ]
