# Generated by Django 5.0.5 on 2024-05-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrollen', '0003_erstelltekontrollen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erstelltekontrollen',
            name='identifier',
            field=models.CharField(max_length=300),
        ),
    ]
