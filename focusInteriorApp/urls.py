from django.urls import path
from focusInteriorApp import views


app_name='focusInteriorApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('appointment/',views.appointment,name='appointment'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),
    path('feature/',views.features,name='feature'),
    path('teams/',views.teams,name='teams'),
    path('testimonial/',views.testimonial,name='testimonial'),


]