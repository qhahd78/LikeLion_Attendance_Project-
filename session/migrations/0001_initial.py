# Generated by Django 2.2.1 on 2021-01-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
