from django.db import models

# Create your models here.


class StudentModell(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_fname = models.CharField(max_length=50)
    student_mname = models.CharField(max_length=50)
    student_lname = models.CharField(max_length=50)
    rollno = models.IntegerField()
    dob = models.CharField(max_length=50)
    address = models.TextField()
    Male = 'M'
    Female = 'F'
    gender = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]
    class_id = models.ForeignKey('ClassModell', on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    fee_status = models.CharField(max_length=50)

    def get_studentid(self):
        return self.student_id

    def getfname(self):
        return self.student_fname

    def getfullname(self):
        return self.student_fname+" "+self.student_lname

    def getrollno(self):
        return self.rollno

    def getdob(self):
        return self.dob

    def getaddress(self):
        return self.address

    def getbloodgroup(self):
        return self.blood_group

    #To access student's parent
    def getparentname(self):
        return self.student_mname+" "+self.student_lname

    def getclassname(self):
        return self.class_id

    def getstatus(self):
        return self.fee_status


class ClassModell(models.Model):
    default_value = '999'
    class_id = models.AutoField(primary_key=True, default=default_value)
    class_name = models.CharField(max_length=10, default='8A')

    def getclassname(self):
        return self.class_name

    def getclassid(self):
        return self.class_id


class ParentModell(models.Model):
    default_value = '999'
    parent_id = models.AutoField(
        primary_key=True, default=default_value, auto_created=True)
    parent_fname = models.CharField(max_length=50, default='null')
    parent_mname = models.CharField(max_length=50, default='null')
    parent_lname = models.CharField(max_length=50, default='null')

    def getparentid(self):
        return self.parent_id

    def getfullname(self):
        return self.parent_fname+" "+self.parent_mname+" "+self.parent_lname


class STmapping(models.Model):
    student_id = models.ForeignKey('StudentModell', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('ParentModell', on_delete=models.CASCADE)

    def getstudent_id(self):
        return self.student_id

    def getparent_id(self):
        return self.parent_id


class StudentParent(models.Model):
    student_id = models.ForeignKey('StudentModell', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('ParentModell', on_delete=models.CASCADE)

    def getstudent_id(self):
        return self.student_id

    def getparent_id(self):
        return self.parent_id


class Student_attendence(models.Model):
    student_id = models.OneToOneField(
        StudentModell, on_delete=models.CASCADE, to_field='student_id', primary_key=True, default=1)
    class_id = models.ForeignKey('ClassModell', on_delete=models.CASCADE)
    attendence_percent = models.IntegerField()
    # def getattnedence_percent(self):
    #     return (self.noofdays_attended/self.total_days)*100

    def getstudent_id(self):
        return self.student_id

    def getclass_id(self):
        return self.class_id

    def getattend(self):
        return self.attendence_percent


class SubjectModell(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=30)
    class_id = models.ForeignKey('ClassModell', on_delete=models.CASCADE)

    def getstubject_id(self):
        return self.subject_id

    def getclass_id(self):
        return self.class_id

    def getsubjname(self):
        return self.subject_name


class Student_marks(models.Model):
    marks_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(
        'StudentModell', on_delete=models.CASCADE, default=1)
    subject_id = models.ForeignKey('SubjectModell', on_delete=models.CASCADE)
    class_id = models.ForeignKey('ClassModell', on_delete=models.CASCADE)
    year = models.IntegerField()
    exam_type = models.ForeignKey('ExamModell', on_delete=models.CASCADE)
    marks = models.IntegerField()
    P = 'Pass'
    F = 'Fail'
    pfstatus = [
        (P, 'P'),
        (F, 'F'),
    ]
    pass_fail = models.CharField(choices=pfstatus, max_length=10)

    def getstudent_id(self):
        return self.student_id

    def getstubject_id(self):
        return self.subject_id

    def getclass_id(self):
        return self.class_id

    def getmark_id(self):
        return self.marks_id

    def getmarks(self):
        return self.marks

    def getexamtype(self):
        return self.exam_type

    def getpassfail(self):
        return self.pass_fail


class ExamModell(models.Model):
    ClassTest = 'Class Test'
    UnitTest = 'Unit Test'
    FinalTest = 'Final Test'
    UnitMarks = 30
    FinalMarks = 70
    ClassMarks = 20
    exam_types = [
        (ClassTest, 'Class Test'),
        (UnitTest, 'Unit Test'),
        (FinalTest, 'Final Test'),
    ]
    exam_tot_marks = [
        (ClassMarks, 20),
        (UnitMarks, 30),
        (FinalMarks, 70),
    ]
    typeexam = models.CharField(max_length=50, choices=exam_types)
    totalexammarks = models.IntegerField(choices=exam_tot_marks)

    def getexamtype(self):
         return self.typeexam

    def getexamtotmarks(self):
        return self.totalexammarks
