from django.db import models

class unit(models.Model):
	pass

class Item(models.Model):
	KeyId=models.ForeignKey(unit,default=None, on_delete=models.CASCADE)
	text=models.TextField(default="")
#	pass

# Create your models here.
