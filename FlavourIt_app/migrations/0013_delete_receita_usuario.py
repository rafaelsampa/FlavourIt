# Generated by Django 4.2.16 on 2024-12-04 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FlavourIt_app', '0012_remove_receita_usuario_id_cliente_receita_id_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='receita_usuario',
        ),
    ]
