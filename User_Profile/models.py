from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#signals sends out information to other parts of the program
#auth is authentication. I'm not quite sure how it works yet
# Create your models here.

class Skills(models.Model):
    user =models.ForeignKey(User)
    skill =models.CharField(db_index=True, max_length=40, null=True)
    yearxp = models.IntegerField(null=True)
    description=models.CharField(max_length=400,null=True)
    
class Desires(models.Model):
    user=models.ForeignKey(User)
    wants = models.CharField(db_index=True, max_length=40, null=True)
    description =models.CharField(max_length=400,null=True)
    
class Askill(models.Model):
    userprofile=models.ForeignKey('UserProfile')
    skill= models.ForeignKey('Skills')
    date_created=models.DateField()
        
class Adesire(models.Model):
    userprofile=models.ForeignKey('UserProfile')
    desire= models.ForeignKey('Desires')
    date_created=models.DateField()   
    
class UserProfile(models.Model):
#This is a start of the user profile page
    user = models.OneToOneField(User)
    #facebook = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    #website = models.CharField(max_length=80, null=True)
    #GENDER_CHOICES = (
    #    ('m', 'Male'),
    #    ('f', 'Female'),
    #    ('n', 'NA')
    #)
    #basic user fields, more probably for later
    #user = models.ForeignKey(User, unique=True)
    #birth_date = models.DateField(null= True)
    #location = models.CharField(max_length=150, null=True)
    skills = models.ManyToManyField(Skills,through='Askill')
    desires = models.ManyToManyField(Desires,through='Adesire')
    city = models.CharField(db_index=True,max_length=400, null=True)
    def __unicode__(self):
        return self.user.username
    

