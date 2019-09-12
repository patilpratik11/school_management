from django.db import models

# Create your models here.
class AdminModel(models.model):
    admin_id = models.AutoField(primary_key=True)
    admin_fname = models.CharField(max_length=50)
    admin_mname = models.CharField(max_length=50)
    admin_lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
		return str(self.admin_id)

	def getPassword(self):
		return self.password

	def getEmail(self):
		return self.email

	def getfName(self):
		return self.first_name

	def getlName(self):
		return self.last_name

	def getId(self):
		return self.admin_id