# Generated by Django 5.0.5 on 2024-05-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrollen', '0007_rename_visibility_kontrollen_sichtbar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrollen',
            name='thema',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
