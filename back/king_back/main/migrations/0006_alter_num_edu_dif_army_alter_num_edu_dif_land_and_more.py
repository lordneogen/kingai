# Generated by Django 4.2.1 on 2023-05-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_num_edu_epoth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num_edu',
            name='dif_army',
            field=models.IntegerField(blank=True, default=1000),
        ),
        migrations.AlterField(
            model_name='num_edu',
            name='dif_land',
            field=models.IntegerField(blank=True, default=1000),
        ),
        migrations.AlterField(
            model_name='num_edu',
            name='dif_money',
            field=models.IntegerField(blank=True, default=100000),
        ),
        migrations.AlterField(
            model_name='num_edu',
            name='dif_popularity',
            field=models.IntegerField(blank=True, default=1000),
        ),
    ]
