"""ProjectList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from BMIList import views


urlpatterns = [
    url(r'^$', views.LogIn, name='login'),
    url(r'^ProjectList/signup$', views.SignUp, name='signup'),
    url(r'^ProjectList/index$', views.Index, name='index'),
    url(r'^ProjectList/peach$', views.Peachy, name='peach'),
    url(r'^ProjectList/bmi$', views.BMI, name='bmi'),
    url('admin/',admin.site.urls),
#    url(r'^BMIList/(\d+)/$', views.ViewList, name='mgm'),
#    url(r'^BMIList/mgm2_url$', views.NewList, name='Newlist'),
#    url(r'^BMIList/(\d+)/addItem$', views.AddItem, name='additem'),
    #path('admin/', admin.site.urls),
]
