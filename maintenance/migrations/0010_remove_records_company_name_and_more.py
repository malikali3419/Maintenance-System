# Generated by Django 4.2.6 on 2023-11-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_records_andrede_name_records_land_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='company_name',
        ),
        migrations.AlterField(
            model_name='records',
            name='andrede_name',
            field=models.CharField(blank=True, default=None, max_length=155, null=True),
        ),
    ]
