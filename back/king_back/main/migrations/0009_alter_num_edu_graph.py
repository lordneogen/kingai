# Generated by Django 4.2.1 on 2023-05-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_cards_is_learn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num_edu',
            name='graph',
            field=models.ImageField(blank=True, null=True, upload_to='\\pic'),
        ),
    ]
