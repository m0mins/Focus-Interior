from django.shortcuts import render
from focusInteriorApp.models import Contact,Appointment
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

import requests

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'focusInteriorApp/index.html')

def about(request):
    return render(request,'focusInteriorApp/about_nav.html')
def appointment(request):
    print("######################################")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        service=request.POST.get('service')
        date=request.POST.get('date')
        time=request.POST.get('time')

        message=request.POST.get('message')
        appoint=Appointment.objects.create(name=name,email=email,phone=phone,service=service,date=date,time=time,message=message)

        appoint.save()
        print("finally saved ######################################")
        email_subject = f'New contact {email}: {service}'
        #email_message = note
        email_message = f'Name : {name}\n Service : {service}\n Message : {message}'

        #recipient_list = settings.EMAIL_HOST_USER
        #from_email = email

        #recipient_list = settings.EMAIL_HOST
        print("print  from inside form method #############******************#######################")
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

        #send_mail(email_subject, email_message, from_email, recipient_list)
        #return redirect("portfolioApp:home")
        return HttpResponseRedirect(reverse('focusInteriorApp:index'))
    #context = {'form': form}
    #return render(request, 'contact/contact.html', context)
    return render(request,'focusInteriorApp/appointment_nav.html')


def service(request):
    return render(request,'focusInteriorApp/service_nav.html')

#def contact(request):
#    return render(request,'focusInteriorApp/contact_nav.html')

def contact(request):

    print("######################################")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact.objects.create(name=name,email=email,subject=subject,message=message)

        contact.save()
        print("finally saved ######################################")
        email_subject = f'New contact {email}: {subject}'
        #email_message = note
        email_message = f'Name : {name}\n Subject : {subject}\n Message : {message}'

        #recipient_list = settings.EMAIL_HOST_USER
        #from_email = email

        #recipient_list = settings.EMAIL_HOST
        print("print  from inside form method #############******************#######################")
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

        #send_mail(email_subject, email_message, from_email, recipient_list)
        #return redirect("portfolioApp:home")
        return HttpResponseRedirect(reverse('focusInteriorApp:index'))
    #context = {'form': form}
    #return render(request, 'contact/contact.html', context)
    return render(request,'focusInteriorApp/contact_nav.html')

def projects(request):
    return render(request,'focusInteriorApp/projects_nav.html')
def features(request):
    return render(request,'focusInteriorApp/feature_nav.html')

def teams(request):
    return render(request,'focusInteriorApp/teams_nav.html')

def testimonial(request):
    return render(request,'focusInteriorApp/testimonial_nav.html')