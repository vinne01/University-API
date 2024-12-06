# Generated by Django 5.1 on 2024-12-06 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_remove_student_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('staff_no', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=30)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.teacher')),
            ],
        ),
    ]