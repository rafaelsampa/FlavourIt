# Generated by Django 5.1.3 on 2024-12-05 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FlavourIt_app', '0013_delete_receita_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='nome',
        ),
    ]