# Generated by Django 2.1.1 on 2018-10-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
    ]
