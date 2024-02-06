from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Offline, Service
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home page")

def about(request):
    return render(request, 'about.html')

def services(request):
    if request.method=="POST":
        icename=request.POST.get('icename')
        special_item=request.POST.get('special_item')
        ice_quantity=request.POST.get('ice_quantity')
        delivery_type=request.POST.get('delivery_type')
        delivery_area=request.POST.get('delivery_area')
        services=Service(icename= icename, special_item=special_item, ice_quantity=ice_quantity,
                         delivery_type=delivery_type ,delivery_area=delivery_area)
        services.save()
        messages.success(request, "Your Order is Confirm")

    return render(request, 'services.html')


def payment(request):
    return render(request, 'payment.html')

def offline(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        address=request.POST.get('address')
        email1=request.POST.get('email1')
        offline=Offline(fname=fname, lname=lname, city=city, zip=zip, address=address, email1=email1)
        offline.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'offline.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")


    return render(request, 'contact.html')