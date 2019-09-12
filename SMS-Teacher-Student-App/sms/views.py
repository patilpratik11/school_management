from django.shortcuts import render
from django.http import HttpResponse
from sms.models import Teacher, ClassTeacher, SubjectTeacher, Subject, Attendance, Marks, Exam, Login, Timetable
from django.contrib import messages
import datetime
from student.models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, ExamModell,SubjectModell, StudentParent, STmapping

# Create your views here.

def index(request):
    return render(request, 'common/index.html') 

def acctype(request):
    return render(request, 'common/accounts.html')    

def studentLogin(request):
	Login.objects.all().delete()
	return render(request, 'common/login_student.html')    

def teach_Login(request):
    id = 1
    Login.objects.all().delete()
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def parent_Login(request):
    id = 2
    Login.objects.all().delete()
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def admin_Login(request):
    id = 3
    Login.objects.all().delete()
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })    

def addsubject(request):
	return render(request, 'common/addsubject.html')

def addmarks(request):
	return render(request, 'common/addmarks.html')

def addattend(request):
	return render(request, 'common/addattend.html')

def addexams(request):
	return render(request, 'common/addexams.html')

def attendance(request):
	roll_list = request.POST.get("absent_list")
	class_name = request.POST.get("class_name")
	date = datetime.date.today()
	
	p = ClassTeacher.objects.get(class_name=class_name)

	q = Attendance(student_roll=int(roll_list), class_name=p, date=date)
	q.save()

	messages.info(request, 'Attendance Added Successfully')

	return render(request, 'common/addattend.html')

def marks(request):

	subject_name = request.POST.get("subject_name")
	student_roll = request.POST.get("student_roll")
	class_name = request.POST.get("class_name")
	marks = request.POST.get("marks")
	exam_type = request.POST.get("exam_type")

	subjectobj = Subject.objects.get(subject_name=subject_name)
	studentobj = Attendance.objects.get(student_roll=student_roll)
	classobj = ClassTeacher.objects.get(class_name=class_name)
	query = Marks(subject_name=subjectobj, student_roll=studentobj, class_name=classobj, marks=marks, exam_type=exam_type)	
	query.save()
	
	messages.info(request, 'Marks Added Successfully')

	return render(request, 'common/addmarks.html')

def exams(request):

	exam_name = request.POST.get("exam_name")	
	subject = request.POST.get("subject")
	total = request.POST.get("total_marks")

	subjectobj = Subject.objects.get(subject_name=subject)
		
	query = Exam(exam_name=exam_name, subject_name=subjectobj, total_marks=total)
	query.save()

	messages.info(request, 'Exam Added Successfully')

	return render(request, 'common/addexams.html')

def subject(request):
	
	subject_name = request.POST.get("subject_name")
	class_name = request.POST.get("class_name")

	loginobj = Login.objects.all().first()
	teacherobj = Teacher.objects.get(teacher_id=loginobj.getId())
	subjectobj = Subject.objects.get(subject_name=subject_name)
	classobj = ClassTeacher.objects.get(class_name=class_name)

	query = SubjectTeacher(teacher_id=teacherobj, subject_id=subjectobj, class_name=classobj)
	query.save()
	
	messages.info(request, 'Subject Added Successfully')

	return render(request, 'common/addsubject.html')

def display_marks(request):

	loginobj = Login.objects.all().first()
	
	try:
		subjectobj = list(SubjectTeacher.objects.filter(teacher_id=loginobj.getId()))	
		
		marks = []
		subject_list = []
		roll = []
		class_n = []
		exam = []
		count = 0

		for obj in subjectobj:	
			subject = Subject.objects.get(subject_id=subjectobj[count].getSubjectString())
			marksobj = list(Marks.objects.filter(subject_name=subject.getSubject(), class_name=subjectobj[count].getClassString()))
			for x in marksobj:				
				marks.append(x.getMarks())
				subject_list.append(x.getSubject())
				roll.append(x.getRoll())
				class_n.append(x.getClass())
				exam.append(x.getExam())
			count = count + 1
		return render(request, 'common/display_marks.html', {'marks':marks, 'subject':subject_list,'roll':roll,'class':class_n,'exam':exam})

	except:				 		
		messages.info(request, 'No Marks Added')
		return render(request, 'common/display_marks.html')

def display_attendance(request):

	loginobj = Login.objects.all().first()

	try:
		classobj = ClassTeacher.objects.get(teacher_id = loginobj.getId())
		
		attendanceobj = list(Attendance.objects.filter(class_name = classobj.getClassStr()))	
		
		roll = []
		class_name = []
		date = []
		
		for obj in attendanceobj:
			roll.append(obj.getRollStr())
			class_name.append(obj.getClassStr())
			date.append(obj.getDateStr())
			
		return render(request, 'common/display_attendance.html', {'roll':roll, 'class':class_name, 'date':date})
			
	except:
		messages.info(request, 'No Marks Added')	
		return render(request, 'common/display_attendance.html')
def display_timetable(request):

	tableobj = Timetable.objects.all()
	
	return render(request, 'common/display_timetable.html' , {'table':tableobj})
	
def changetable(request):

	return render(request, 'common/changetimetable.html')

def timetable(request):
	
	try:
		day = request.POST.get("day")
		period = request.POST.get("period")
		subject = request.POST.get("subject")
		
		if day == "Monday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Monday = subject
			tableobj.save()
			
		if day == "Tuesday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Tuesday = subject
			tableobj.save()
			
		if day == "Wednesday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Wednesday = subject
			tableobj.save()
			
		if day == "Thursday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Thursday = subject
			tableobj.save()
			
		if day == "Friday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Friday = subject
			tableobj.save()
			
		if day == "Saturday":
			tableobj = Timetable.objects.get(id = period)
			tableobj.Saturday = subject
			tableobj.save()
			
		messages.info(request, 'Timetable Changed')		
		return render(request, 'common/changetimetable.html')

	except:		
		messages.info(request, 'No Changes Added')		
		return render(request, 'common/changetimetable.html')

def loginstudent(request):	
	
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		dob = request.POST.get("dob")
		
		studentobj = StudentModell.objects.get(student_fname=first_name, student_lname=last_name)
		
		if studentobj.dob == dob:
			
			attendence = Student_attendence.objects.filter(class_id_id = studentobj.class_id)
			classinfo = studentobj.class_id
			temp = studentobj.student_id
			stmappingobject = STmapping.objects.get(student_id=temp)
			parentobject = stmappingobject.parent_id
			return render(request, 'common/studentDashboard.html', {'dbuser':studentobj, 'attendence':attendence,'classinfo':classinfo, 'parentobject':parentobject})	
		
		else:		
			messages.info(request, 'Invalid credentials')
			return render(request, 'common/login_student.html')
	
def loginTeacher(request):
	
	email_id = request.POST.get("email")
	password = request.POST.get("password")

	query = Teacher.objects.get(email=email_id)

	if password == query.getPassword():
		first_name = query.getfName()
		last_name = query.getlName()
		id = query.getId()
		
		loginobj = Login(teacher_id=query)
		loginobj.save()

		try:
			classobj = ClassTeacher.objects.get(teacher_id=id)
			class_name = classobj.getClass()
		except:
			class_name = "null"
		
		try:
			subjects=list(SubjectTeacher.objects.filter(teacher_id=id))
		
			subject_name = []
			class_names = []

			for subjectobj in subjects:		
				s_id = subjectobj.getSubject()
				subject = Subject.objects.get(subject_id=s_id.subject_id)
				subject_name.append(str(subject.getSubjectName()))
				class_names.append(str(subjectobj.getClass()))
		except:
			subject_name = "null"

		return render(request, 'common/success.html', {'first':first_name, 'last':last_name, 'id':id, 'class':class_name, 'subject':subject_name, 'classes':class_names})
	else:
		messages.info(request, 'Invalid credentials')
		return render(request, 'common/teach_parent_admin_login.html', {"id" : 1 })
