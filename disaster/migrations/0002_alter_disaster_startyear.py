# Generated by Django 4.1.7 on 2023-03-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='startYear',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
