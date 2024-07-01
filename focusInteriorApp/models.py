from django.db import models

# To Create a Custom User Model and Admin Panel

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy

# To automatically create one to one objects

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUserManager(BaseUserManager):
    """ A custom Manager to deal with emails as unique identifer """
    def _create_user(self, email, password, **extra_fields):
        """ Creates and saves a user with a given email and password"""

        if not email:
            raise ValueError("The Email must be set!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(unique=True, null=False)
    is_varified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text = gettext_lazy('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=264, blank=True,null=True)
    #last_name = models.CharField(max_length=264, blank=True)
    designation = models.CharField(max_length=20, blank=True,null=True)
    email = models.EmailField(unique=True, null=False,blank=False)
    image=models.ImageField(upload_to='prof_pic')
    address_1 = models.TextField(max_length=300, blank=True,null=True)
    city = models.CharField(max_length=40, blank=True,null=True)
    zipcode = models.CharField(max_length=10, blank=True,null=True)
    country = models.CharField(max_length=50, blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True,null=True)
    github = models.CharField(max_length=100, blank=True,null=True)
    linkedIn = models.CharField(max_length=100, blank=True,null=True)
    twitter = models.CharField(max_length=100, blank=True,null=True)
    facebook = models.CharField(max_length=100, blank=True,null=True)


    about = models.TextField()
    summary = models.TextField(blank=True,null=True)


    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name + "'s Profile"
#    
#    def is_fully_filled(self):
#        fields_names = [f.name for f in self._meta.get_fields()]
#
#        for field_name in fields_names:
#            value = getattr(self, field_name)
#            if value is None or value=='':
#                return False
#        return True
#
#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#
#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
#    instance.profile.save()

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    subject = models.CharField(max_length=100, null=True,blank=True)
    message = models.TextField( null=True,blank=True)

    def __str__(self):
        return self.subject   
    
class Appointment(models.Model):

    SERVICE_CHOICES = [
        ('service1', 'Service One'),
        ('service2', 'Service Two'),
        ('service3', 'Service Three')
    ]
    name = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=50, null=True,blank=True)
    service = models.CharField(max_length=50,unique=True, choices=SERVICE_CHOICES, default='service3')

    date = models.DateField(max_length=100, null=True,blank=True)
    time = models.TimeField(max_length=100, null=True,blank=True)

    message = models.TextField( null=True,blank=True)

    def __str__(self):
        return self.service   