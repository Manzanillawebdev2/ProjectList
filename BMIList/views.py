from django.shortcuts import redirect, render
from django.http import HttpResponse
from BMIList.models import LogIn,SignUp,Index

# Create your views here.

#BmiPage = None
def LogIn(request):
	return render (request, 'login.html')
	
def SignUp(request):
	return render (request, 'signup.html')
	Item.object.create(email=request.POST ['email'],
	psw=request.POST ['psw'], repeat=request.POST ['repeat'],
	fname=request.POST ['fname'], lname=request.POST ['lname'],
	age=request.POST ['age'], sex=request.POST ['sex'])
	return redirect (f'login.html')
	
def Index(request):
	return render (request, 'index.html')
	
def Peachy(request):
	return render (request, 'exercise.html')
	
def BMI(request):
	return render (request, 'bmi.html')
	
#def BmiPage(request):
#  return render (request, 'bmi.html')	
  	
#  items = Item.objects.all()
  #else:
#  	newItem=''

#  return render (request, 'bmi.html', {'Age':items})
  
  
#def ViewList(request, KeyId):
#	KId = unit.objects.get(id=KeyId)
#	items = Item.objects.all()
#	items = Item.objects.filter(KeyId=KId)
#	return render (request, 'bmicalcu.html', {'KId':KId})
	
#def NewList(request):
#	newunit = unit.objects.create()
#	Item.objects.create(KeyId=newunit, text=request.POST['age'])
#	return redirect(f'/BMIList/{newunit.id}/')
	
#def AddItem(request, KeyId):
#	KId = unit.objects.get(id=KeyId)
#	Item.objects.create(KeyId=KId, text=request.POST['age'])
#	return redirect(f'/BMIList/{KId.id}/')
	

'''	
def NewList(request):
	Item.objects.create(text=request.POST['age'])
	return redirect('/BMIList/mgm2_url/')'''
	
