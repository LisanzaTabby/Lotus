# Generated by Django 5.1 on 2024-09-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0022_alter_studentdonorhistory_school_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdonorhistory',
            name='school_level',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='studentdonorhistory',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='AcademicProgress',
        ),
    ]
