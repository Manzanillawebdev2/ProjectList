from django.shortcuts import redirect, render
from django.http import HttpResponse
from BMIList.models import LogIn,SignUp, InputData, Rate


# Create your views here.

#BmiPage = None
def LogIn(request):
	return render (request, 'login.html')
	
def SignUpp(request):
	return render (request, 'signup.html')
	

def new(request):
	NewUser= SignUp.objects.create(meyl=request.POST['meyll'],
	psw=request.POST ['psww'],
	fname=request.POST ['fnamee'], lname=request.POST ['lnamee'],
	age=request.POST ['agge'], sex=request.POST ['ssex'])
	return redirect(f'/bmi/{NewUser.id}/')

def ViewData(request, UserId):
	uId = SignUp.objects.get(id=UserId)
	return render (request, 'bmi.html', {'uId': uId})

def AddDataBmi(request, UserId):
#	pass
	uId= SignUp.objects.get(id=UserId)
	Input = InputData(Date=request.POST['date'],  
	Height=request.POST['height'], 
	Weight=request.POST['weight'], 
	BMITotal=request.POST['total'], 
	BMIResult=request.POST['result'], SignUp=uId,)
	Input.save()
	return redirect (f'/bmi/{uId.id}/')

def HistoryPage(request, UserId):
	Input = InputData.objects.all()
	uId= SignUp.objects.get(id=UserId)
	return render (request, 'history.html', {'InputData':Input})

def UpdateHis(request, id):
	signup= SignUp.objects.get(id=id) #OK
	content = {'signup':signup}
	return render (request, 'signupdate.html', content) 

def DataChange (request,id):
	signup= SignUp.objects.get(id=id)
	signup.meyl=request.POST['meyll']
	signup.psw=request.POST['psww']
	signup.fname=request.POST['fnamee']
	signup.lname=request.POST['lnamee']
	signup.age=request.POST['agge']
	signup.sex=request.POST['ssex']
	signup.save()
	return redirect('login')

def DeleteDon (request,id):
	inputdata = InputData.objects.get(id=id)
	inputdata.delete()
	return redirect('/')

def BenefitPage(request, UserId):
	uId = SignUp.objects.get(id=UserId)
	return render (request, 'index.html', {'uId':uId})

def FitPage(request, UserId):
	uId = SignUp.objects.get(id=UserId)
	return render (request, 'exercise.html', {'uId':uId})

def AboutPage(request, UserId):
	uId = SignUp.objects.get(id=UserId)
	return render (request, 'about.html', {'uId':uId})

def AddRate(request, UserId):
	uId = SignUp.objects.get(id=UserId)
	Rate.objects.create(Rating=request.POST ['star'], SignUp=uId,
	Message=request.POST ['mess'])
	return redirect(f'/bmi/{uId.id}/fitpage')

def home(request): 
 if request.method == 'POST':
        if Signup.objects.filter(fname=request.POST['fnamee'], psw=request.POST['psww']).exists():
            uId = Signup.objects.get(fname=request.POST['fnamee'], psw=request.POST['pswws'])
            return redirect(f'/bmi/{uId.id}/benefitpage')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)

#def section2(request):
#	return render (request, 'index3.html')

#def section3(request):
#	return render (request, 'index4.html')

#def section4(request):
#	return render (request, 'index5.html')

#def update(request, UserId):
#	uId= SignUp.objects.get(id=UserId)
#	Input = InputData(Date=request.POST['date'],  
#	Height=request.POST['height'], 
#	Weight=request.POST['weight'], 
#	BMITotal=request.POST['total'], 
#	BMIResult=request.POST['result'], SignUp=uId,)
#	Input.save()
#	return redirect (f'/bmi/{uId.id}/')

	
#def Index(request):
#	return render (request, 'index.html')
	
#def Peachy(request):
#	return render (request, 'exercise.html')
	
#def BMI(request):
#	return render (request, 'bmi.html')
	
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
	
