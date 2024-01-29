# Generated by Django 4.2.5 on 2023-11-07 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0003_resource_acquisition_date_resource_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='acquisition_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='resource',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, default='Description'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='location',
            field=models.CharField(blank=True, default='Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(blank=True, default='Resource Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='resource',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='resource',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('Water', 'Water'), ('Medical Supplies', 'Medical Supplies'), ('Equipment', 'Equipment'), ('Other', 'Other')], default='Other', max_length=50),
        ),
        migrations.AlterField(
            model_name='resource',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('L', 'Liter'), ('unit', 'Unit'), ('box', 'Box'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]