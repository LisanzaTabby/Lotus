# Generated by Django 5.1 on 2024-09-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0018_alter_studentdonorhistory_changed_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprogress',
            name='school_level',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='academicprogress',
            name='year',
            field=models.IntegerField(),
        ),
    ]
