# Generated by Django 5.1.2 on 2024-10-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlavourIt_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores_nutricionais',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]