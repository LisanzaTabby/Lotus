# Generated by Django 5.1 on 2024-08-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0009_rename_level_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(blank=True, choices=[('PrimaryOnly', 'PrimaryOnly'), ('Primary&Secondary', 'Primary&Secondary'), ('Primary&Secondary&Tertiary', 'Primary&Secondary&Tertiary'), ('Secondary&tertiary', 'Secondary&tertiary'), ('TertiaryOnly', 'TertiaryOnly'), ('SecondaryOnly', 'SecondaryOnly'), ('Primary&Tertiary', 'Primany&Tertiary')], max_length=100, null=True),
        ),
    ]