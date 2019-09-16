# Generated by Django 2.2.5 on 2019-09-12 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModell',
            fields=[
                ('class_id', models.AutoField(default='999', primary_key=True, serialize=False)),
                ('class_name', models.CharField(default='8A', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExamModell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeexam', models.CharField(choices=[('Class Test', 'Class Test'), ('Unit Test', 'Unit Test'), ('Final Test', 'Final Test')], max_length=50)),
                ('totalexammarks', models.IntegerField(choices=[(20, 20), (30, 30), (70, 70)])),
            ],
        ),
        migrations.CreateModel(
            name='ParentModell',
            fields=[
                ('parent_id', models.AutoField(auto_created=True, default='999', primary_key=True, serialize=False)),
                ('parent_fname', models.CharField(default='null', max_length=50)),
                ('parent_mname', models.CharField(default='null', max_length=50)),
                ('parent_lname', models.CharField(default='null', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModell',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_fname', models.CharField(max_length=50)),
                ('student_mname', models.CharField(max_length=50)),
                ('student_lname', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('dob', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('blood_group', models.CharField(max_length=5)),
                ('fee_status', models.CharField(max_length=50)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassModell')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectModell',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=30)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassModell')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ParentModell')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell')),
            ],
        ),
        migrations.CreateModel(
            name='Student_marks',
            fields=[
                ('marks_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('pass_fail', models.CharField(choices=[('Pass', 'P'), ('Fail', 'F')], max_length=10)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassModell')),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ExamModell')),
                ('student_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.SubjectModell')),
            ],
        ),
        migrations.CreateModel(
            name='STmapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ParentModell')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell')),
            ],
        ),
        migrations.CreateModel(
            name='Student_attendence',
            fields=[
                ('student_id', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='student.StudentModell')),
                ('attendence_percent', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ClassModell')),
            ],
        ),
    ]