# Generated by Django 5.0.5 on 2024-05-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrollen', '0008_alter_kontrollen_thema'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontrollen',
            name='beispiel',
            field=models.BooleanField(default=False),
        ),
    ]