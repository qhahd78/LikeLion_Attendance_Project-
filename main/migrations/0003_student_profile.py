# Generated by Django 3.1.5 on 2021-01-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210119_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]