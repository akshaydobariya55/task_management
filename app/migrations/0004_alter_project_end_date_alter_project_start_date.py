# Generated by Django 4.2.3 on 2023-10-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
    ]
