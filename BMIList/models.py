from django.db import models

class LogIn(models.Model):
	pass
#	lsignup=models.ForeignKey (SignUp, default=None, on_delete=models.CASCADE)
#	psw=models.ForeignKey (SignUp, default=None, on_delete=models.CASCADE)
	
#	class meta:
#		db_table= "LogIn"
		
class Index(models.Model):
	pass
class SignUp(models.Model):
	email=models.TextField(default="")
	psw=models.TextField(default="")
	repeat=models.TextField(default="")
	fname=models.TextField(default="")
	lname=models.TextField(default="")
	age=models.TextField(default="")
	sex=models.TextField(default="")
	
	class meta:
		db_table= "SignUp"		
class IndexStatus(models.Model):
	SignUp=models.ForeignKey(SignUp,default=None, on_delete=models.CASCADE)
	Status=models.TextField(default="")
	class meta:
		db_table="Index Status"
		
class EProgram(models.Model):
	SignUp=models.ForeignKey(SignUp,default=None, on_delete=models.CASCADE)
	Plan=models.TextField(default="")
	class meta:
		db_table="Enroll Program"
		
class CheckStatus(models.Model):
	SignUp=models.ForeignKey(SignUp,default=None, on_delete=models.CASCADE)
	Date=models.DateTimeField(auto_now_add=True, null=True)
	CurrentWeight=models.TextField(default="")
	Remarks=models.TextField(default="")
	class meta:
		db_table="Check Status"

class Record(models.Model):
	Eprogram=models.ForeignKey(EProgram,default=None, on_delete=models.CASCADE)
	CheckStatus=models.ForeignKey(CheckStatus,default=None, on_delete=models.CASCADE)
	class meta:
		db_table="Record"

#	pass

# Create your models here.
#class Item(models.Model):
#	KeyId=models.(unit,default=None, on_delete=models.CASCADE)
#	text=models.TextField(default="")
#	pass

# Create your models here.
