# Generated by Django 4.2.3 on 2023-11-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_task_project_name_task_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_name',
        ),
    ]
