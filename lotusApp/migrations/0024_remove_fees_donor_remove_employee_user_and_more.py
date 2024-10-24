# Generated by Django 5.1 on 2024-09-15 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0023_alter_studentdonorhistory_school_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='examresults',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='examresults',
            name='student',
        ),
        migrations.AlterUniqueTogether(
            name='fees',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='student',
            name='intermediary',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tertiary_school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='secondary_school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='primary_school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='studentdonorhistory',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentdonorhistory',
            name='donor',
        ),
        migrations.DeleteModel(
            name='Donor',
        ),
        migrations.DeleteModel(
            name='Fees',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='ExamResults',
        ),
        migrations.DeleteModel(
            name='Intermediary',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentDonorHistory',
        ),
    ]
