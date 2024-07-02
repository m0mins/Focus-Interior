from django.contrib import admin
from focusInteriorApp.models import Profile,CompanyProfile,Contact,Appointment,EmployeeProfile,Projects,Project_Work,OurWork
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import BaseInlineFormSet

class Project_WorkInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Ensure that at least one size is selected
        if not any(form.cleaned_data.get('title') for form in self.forms):
            raise ValidationError('You must select at least one point of summary.')
class Product_SizeInline(admin.TabularInline):
    model = Project_Work
    formset = Project_WorkInlineFormSet




admin.site.register(Profile)
admin.site.register(CompanyProfile)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(EmployeeProfile)
admin.site.register(Projects)
admin.site.register(OurWork)

admin.site.register(Project_Work)
