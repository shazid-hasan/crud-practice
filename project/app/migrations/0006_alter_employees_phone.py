# Generated by Django 4.2.7 on 2023-11-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_employees_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.IntegerField(default='000'),
        ),
    ]
