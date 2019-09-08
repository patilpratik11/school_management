from django.db import models

# Create your models here.
class Student_information(models.Model):
    sid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        db_table = "student_info"


