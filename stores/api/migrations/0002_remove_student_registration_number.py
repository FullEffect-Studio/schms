# Generated by Django 5.0.6 on 2024-12-25 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='registration_number',
        ),
    ]