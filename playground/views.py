from django.shortcuts import render
from django.http import HttpResponse


def landingPage(request):
    context = {}
    return render(request, 'landingPage.html', context)

def signIn(request):
    context = {}
    return render(request, 'SignIn.html', context)

def signUp(request):
    context = {}
    return render(request, 'SignUp.html', context)

def homePage(request):
    context = {}
    return render(request, 'HomePage.html', context)
def homeUser(request):
    context={}
    return render(request,'homePageUser.html',context)
def Api_Conection(request):
    context={}
    return render(request,'Api_Connection.html',context)
def stats(request):
    context={}
    return render(request,'stats.html',context)
def Settings(request):
    context={}
    return render(request,'Settings.html',context)
def Price(request):
    context={}
    return render(request,'precio.html',context)

