# Generated by Django 5.1 on 2024-08-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0005_alter_student_backgroundinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profilePic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
