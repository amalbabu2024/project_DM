# Generated by Django 4.2.5 on 2023-11-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0005_remove_resource_expiry_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='acquisition_date',
        ),
    ]