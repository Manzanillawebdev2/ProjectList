from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#BmiPage = None
def BmiPage(request):
    return HttpResponse('<html><head><title>"BMICalculator"</title></head><body><h1>Body Mass Index Calculator</h1><p>Enter your height: <input type="text" id="height"/><select type="multiple" id="heightunits"><option value="metres" selected="selected">metres</option><option value="inches">inches</option></select></p><p>Enter your weight: <input type="text" id="weight"/><select type="multiple" id="weightunits"><option value="kg" selected="selected">kilograms</option><option value="lb">pounds</option></select></p><input type="submit" value="computeBMI" onclick="computeBMI();"><h1>Your BMIis: <span id="output">?</span></h1><h2>This means you are: value = "output" </h2></body></html>') 
