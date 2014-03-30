from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#signals sends out information to other parts of the program
#auth is authentication. I'm not quite sure how it works yet
# Create your models here.
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
    #skills = models.ForeignKey(Skills, null=True)
    ##desires = models.ForeignKey(Desires, null=True)
    city = models.CharField(max_length=400, null=True)
    def __unicode__(self):
        return self.user.username
    
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#
#
#post_save.connect(create_user_profile, sender=User)
