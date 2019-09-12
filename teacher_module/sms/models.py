from django.db import models
import datetime

# Create your models here.

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True) 
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	password = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.teacher_id)

	def getPassword(self):
		return self.password

	def getEmail(self):
		return self.email

	def getfName(self):
		return self.first_name

	def getlName(self):
		return self.last_name

	def getMobile(self):
		return self.mobile

	def getId(self):
		return self.teacher_id

class ClassTeacher(models.Model):
	#foreign key teacher_id
	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=100, primary_key=True)
	
	def __str__(self):
 		return self.class_name
	
	def getClass(self):
		return self.class_name
	
	def getClassStr(self):
		return str(self.class_name)
			

class Subject(models.Model):
	#primary key subject_id
	subject_id = models.AutoField(primary_key=True)	
	subject_name = models.CharField(max_length=100, unique=True)
	
	def __str__(self):
 		return str(self.subject_id)

	def getSubject(self):
		return str(self.subject_id)

	def getSubjectName(self):
		return str(self.subject_name)
	

class SubjectTeacher(models.Model):
	#foreign key teacher_id subject_id class

	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)

	def getSubject(self):
		return self.subject_id

	def getSubjectString(self):
		return str(self.subject_id)

	def getClass(self):
		return self.class_name

	def getClassString(self):
		return str(self.class_name)

class Attendance(models.Model):
	student_roll = models.IntegerField()
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)
	date = models.DateField()
	
	def __str__(self):
 		return str(self.student_roll)

	def getRoll(self):
		return self.student_roll
	
	def getClass(self):
		return self.class_name
		
	def getRollStr(self):
		return str(self.student_roll)
	
	def getClassStr(self):
		return str(self.class_name)
	
	def getDateStr(self):
		return str(self.date)

class Marks(models.Model):
	subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	student_roll = models.ForeignKey(Attendance, on_delete=models.CASCADE)
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)
	marks = models.IntegerField()
	exam_type = models.CharField(max_length=100)

	def getSubject(self):
		return str(self.subject_name)

	def getRoll(self):
		return str(self.student_roll)

	def getMarks(self):
		return str(self.marks)

	def getExam(self):
		return str(self.exam_type)

	def getClass(self):
		return str(self.class_name)

class Exam(models.Model):
	exam_name = models.CharField(max_length=100)
	subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	total_marks = models.IntegerField()

	def getExam(self):
		return self.exam_name

	def getTotal(self):
		return self.total_marks

class Login(models.Model):

	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	
	def getId(self):
		return str(self.teacher_id)
		
class Timetable(models.Model):
	Monday = models.CharField(max_length=100)
	Tuesday = models.CharField(max_length=100)
	Wednesday = models.CharField(max_length=100)
	Thursday = models.CharField(max_length=100)
	Friday = models.CharField(max_length=100)
	Saturday = models.CharField(max_length=100)
	
	def getMonday(self):
		return self.Monday
	
	def getTuesday(self):
		return self.Tuesday

	def getWednesday(self):
		return self.Wednesday
	
	def getThursday(self):
		return self.Thursday
	
	def getFriday(self):
		return self.Friday
	
	def getSaturday(self):
		return self.Saturday
