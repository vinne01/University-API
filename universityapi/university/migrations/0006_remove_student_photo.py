# Generated by Django 5.1 on 2024-12-06 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_remove_teacher_employee_id_student_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
    ]
