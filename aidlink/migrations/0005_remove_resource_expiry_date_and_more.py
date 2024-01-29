# Generated by Django 4.2.5 on 2023-11-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0004_alter_resource_acquisition_date_alter_resource_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='expiry_date',
        ),
        migrations.AlterField(
            model_name='resource',
            name='acquisition_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='resource',
            name='unit',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]