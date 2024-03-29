# Generated by Django 4.2.5 on 2023-12-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twamitraApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
                ('percentage', models.CharField(choices=[('25%', '25'), ('50%', '50'), ('75%', '75'), ('100%', '100')], default='25%', max_length=20)),
            ],
        ),
    ]
