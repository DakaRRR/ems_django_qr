# Generated by Django 4.0.3 on 2022-05-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0006_remove_employees_iin'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='sort_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='sort_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
