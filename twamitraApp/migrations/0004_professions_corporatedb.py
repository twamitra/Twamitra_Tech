# Generated by Django 4.2.5 on 2023-12-15 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twamitraApp', '0003_generatedcode_is_redeemed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CorporateDB',
            fields=[
                ('cid', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('businessName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('referralCode', models.CharField(max_length=8, null=True, unique=True)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twamitraApp.professions')),
            ],
        ),
    ]
