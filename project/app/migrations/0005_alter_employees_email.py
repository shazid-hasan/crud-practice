# Generated by Django 4.2.7 on 2023-11-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_employees_address_alter_employees_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]