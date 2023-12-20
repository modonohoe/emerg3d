# Generated by Django 3.2.3 on 2023-12-20 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryticket',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='€ amount (optional)', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]