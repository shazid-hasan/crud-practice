# Generated by Django 4.2.7 on 2023-11-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_employees_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
