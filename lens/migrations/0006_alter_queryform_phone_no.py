# Generated by Django 5.0.7 on 2024-07-22 09:42

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lens', '0005_alter_queryform_reference_alter_queryform_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryform',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
