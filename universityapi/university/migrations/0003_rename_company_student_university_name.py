# Generated by Django 5.1 on 2024-12-06 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='company',
            new_name='university_name',
        ),
    ]
