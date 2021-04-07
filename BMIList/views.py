from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#BmiPage = None
def BmiPage(request):
#    return HttpResponse('<html><head><title>"BMICalculator"</title></head><body><h1>Body Mass Index Calculator</h1><form><input id="height" name="height" type="text" placeholder="what is your height (in inches)?"> <br><br><input id="weight" name="weight" type="text" placeholder="what is your weight (in kg)?"> <br><input type="submit" id="enter" name="enter" value="enter"></form><p>Your BMIis: <span id="output">?</span></p><p>This means you are: value = "output" </p> </body></html>')
    return render (request, "bmi.html") 
