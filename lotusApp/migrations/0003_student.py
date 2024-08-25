# Generated by Django 5.1 on 2024-08-25 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotusApp', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dateofbirth', models.DateField()),
                ('backgroundInfo', models.TextField()),
                ('profilePic', models.FileField(blank=True, upload_to='profile_pics')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusApp.donor')),
                ('intermediary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusApp.intermediary')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusApp.school')),
            ],
        ),
    ]
