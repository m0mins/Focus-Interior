from django.shortcuts import render
from focusInteriorApp.models import Contact,Appointment,CompanyProfile,EmployeeProfile,Projects,OurWork,Project_Work
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

import requests

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def index(request):
    company_prof=CompanyProfile.objects.all()[0]
    team_members=EmployeeProfile.objects.all()
    projects=Projects.objects.all()
    product_details = []

    for proj in projects:
        all_tasks = proj.project.all()
        product_detail = {
            'projects':projects,
            'name': proj.name,
            'title': proj.title,
            'short_description': proj.short_description,
            'address': proj.address,
            'email': proj.email,
            'image': proj.image,


            'points': [point.task.title for point in all_tasks],
        }

        product_details.append(product_detail)
    combined_data = [{'object': obj, 'project_name': name} for obj, name in zip(projects, product_details)]

    context = {
        'company_prof': company_prof,
        'team_members':team_members,
        'combined_data':combined_data,
        
        }
    return render(request,'focusInteriorApp/index.html',context)

def about(request):
    return render(request,'focusInteriorApp/about_nav.html')
def appointment(request):
    print("######################################")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        service=request.POST.get('service')
        date_input=request.POST.get('date')
        time_input=request.POST.get('time')
        #try:
            # Convert date input to the correct format
        #date_value = datetime.strptime(date_input, '%Y-%m-%d').date()
        #print(f"###############*************3#################{date_value}")

        #except ValueError:
        #return render(request, 'focusInteriorApp/appointment_nav.html', {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

        #try:
            # Convert time input to the correct format
        #time_value = datetime.strptime(time_input, '%H:%M').time()
        #print(f"###############*************3#################{time_value}")
        #except ValueError:
        #return render(request, 'focusInteriorApp/appointment_nav.html', {'error': 'Invalid time format. Please use HH:MM.'})
        message=request.POST.get('message')
        appoint=Appointment.objects.create(name=name,email=email,phone=phone,service=service,date=date_input,time=time_input,message=message)

        appoint.save()
        print("finally saved ######################################")
        email_subject = f'New contact {email}: {service}'
        #email_message = note
        email_message = f'Name : {name}\n Date : {date_input}\n Time : {time_input}\n Service : {service}\n Message : {message}'

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
    membersr=EmployeeProfile.objects.all()
    context = {'membersr': membersr}
    return render(request,'focusInteriorApp/teams_nav.html',context)

def testimonial(request):
    return render(request,'focusInteriorApp/testimonial_nav.html')

def company_profile(request):
    company_prof=CompanyProfile.objects.all()[0]
    return render()
