# Generated by Django 2.2.5 on 2019-09-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datez', models.DateField()),
                ('holidayname', models.CharField(max_length=100)),
            ],
        ),
    ]