from django.db import models

# Create your models here.
class AdminModel(models.Model):
	adm_id = models.AutoField(primary_key=True, default=99) 
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	password = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.adm_id)

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
		return self.adm_id
