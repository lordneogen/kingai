# Generated by Django 4.2.1 on 2023-05-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_cards_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='graph',
            field=models.TextField(default=''),
        ),
    ]