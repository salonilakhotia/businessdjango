# Generated by Django 2.2.6 on 2019-11-03 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20191103_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='contact',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
        migrations.AlterField(
            model_name='staffdetail',
            name='contact',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
    ]
