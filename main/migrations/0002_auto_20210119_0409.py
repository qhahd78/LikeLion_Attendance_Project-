# Generated by Django 3.1.5 on 2021-01-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_num',
            field=models.CharField(max_length=11),
        ),
    ]