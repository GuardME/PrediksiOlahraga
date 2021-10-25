# Generated by Django 3.2.8 on 2021-10-25 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(13), django.core.validators.MaxValueValidator(19)]),
        ),
    ]
