# Generated by Django 5.1 on 2024-09-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0007_feecommitment_year_alter_feecommitment_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feecommitment',
            old_name='Donor',
            new_name='donor',
        ),
    ]
