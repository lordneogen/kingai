# Generated by Django 4.2.1 on 2023-05-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_epoth_num_edu_epo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='is_learn',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
