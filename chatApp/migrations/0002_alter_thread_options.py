# Generated by Django 5.0.1 on 2024-01-13 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-created_at']},
        ),
    ]