# Generated by Django 5.0.6 on 2024-12-25 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_student_registration_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]