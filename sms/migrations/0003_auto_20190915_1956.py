# Generated by Django 2.2.5 on 2019-09-15 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20190914_2348'),
        ('sms', '0002_auto_20190915_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='student_roll',
        ),
        migrations.AddField(
            model_name='marks',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell'),
        ),
    ]
