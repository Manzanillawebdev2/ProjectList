from django.shortcuts import redirect, render
from django.http import HttpResponse
from BMIList.models import Item, unit

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
  
  
def ViewList(request, KeyId):
	KId = unit.objects.get(id=KeyId)
#	items = Item.objects.all()
#	items = Item.objects.filter(KeyId=KId)
	return render (request, 'bmicalcu.html', {'KId':KId})
	
def NewList(request):
	newunit = unit.objects.create()
	Item.objects.create(KeyId=newunit, text=request.POST['age'])
	return redirect(f'/BMIList/{newunit.id}/')
	
def AddItem(request, KeyId):
	KId = unit.objects.get(id=KeyId)
	Item.objects.create(KeyId=KId, text=request.POST['age'])
	return redirect(f'/BMIList/{KId.id}/')
	

'''	
def NewList(request):
	Item.objects.create(text=request.POST['age'])
	return redirect('/BMIList/mgm2_url/')'''
	
