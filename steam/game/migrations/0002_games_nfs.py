# Generated by Django 4.1.5 on 2023-02-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='nfs',
            field=models.BooleanField(default=False),
        ),
    ]