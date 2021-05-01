from django.shortcuts import redirect, render
from django.http import HttpResponse
from BMIList.models import Item

# Create your views here.

#BmiPage = None
def BmiPage(request):
#  if request.method =='POST':
#  	newItem = request.POST['age']
#  	Item.objects.create(text=request.POST['age'])	
#  	return redirect('/BMIList/mgm_url/')
  return render (request, 'bmi.html')	
  	
#  items = Item.objects.all()
  #else:
#  	newItem=''

#  return render (request, 'bmi.html', {'Age':items})
  
  
def ViewList(request):
	items = Item.objects.all()
	return render (request, 'bmicalcu.html', {'Age':items})
	
def NewList(request):
	Item.objects.create(text=request.POST['age'])
	return redirect('/BMIList/mgm_url/')
'''	
def NewList(request):
	Item.objects.create(text=request.POST['age'])
	return redirect('/BMIList/mgm2_url/')'''
	
