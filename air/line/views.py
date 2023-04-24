from django.shortcuts import render, HttpResponse, redirect
from line.models import contact,book_flight,add_flight
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    messages.success(request, 'JET-1 how can we help you!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact_(request):
    if request.method == "POST":
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        co = contact.objects.create(email=email, desc=desc, date=datetime.today())
        co.save()
        messages.success(request, 'your message has been sent!')
    return render(request, "contact.html")

def bookflight(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        contact = request.POST.get("contact")
        frm = request.POST.get("frm")
        to = request.POST.get("to")
        co = book_flight.objects.create(name=name,contact=contact, frm=frm, to=to, date=datetime.today())
        co.save()
        messages.success(request, 'your flight has been booked!')
    return render(request, "bookflight.html")

def flightschedule(request):
    schedule = add_flight.objects.all()
    print(schedule)
    return render(request, "flightschedule.html", {'schedule':schedule})

def adminuse(request):
    return render(request,"adminuse.html")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)

        else:
            return HttpResponse("invalid credentials, please check your username and password")#ye message ma hona chahiye
            #return redirect('/')
        return render(request,'adminpanel.html')

    return HttpResponse("404- Not Found")

def handlelogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/adminuse")
def adminpanel(request):
    messages.success(request,"you are logedin")
    return render(request,'adminpanel.html')

@login_required(login_url="/adminuse")
def addflights(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        duration = request.POST.get("fd")
        frm = request.POST.get("frm")
        to = request.POST.get("to")
        save = add_flight.objects.create(name=name,duration=duration, frm=frm, to=to, date=datetime.today())
        save.save()
    return render(request,'addflight.html')

@login_required(login_url="/adminuse")
def delflight(request):
    schedule = add_flight.objects.all()
    return render(request, "delflight.html", {'schedule':schedule})

def delete(request, id):
    flightschedule = add_flight.objects.get(id = id)
    flightschedule.delete()
    return render(request, "delflight.html")

def checkflight(request):
    data = book_flight.objects.filter(name__startswith='ali').values()
    print(data)
    return render(request, "checkflight.html",{'mydata':data})

def cancelflight(request, id):
    cancel = book_flight.objects.get(id=id)
    cancel.delete()
    return render(request,"checkflight.html")
