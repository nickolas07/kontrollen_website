# Generated by Django 5.0.5 on 2024-06-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrollen', '0009_kontrollen_beispiel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrollen',
            name='identifier',
            field=models.CharField(default='', help_text='Name, welchen die Python Dateien besitzen (ohne .py)', max_length=300, unique=True),
        ),
    ]
