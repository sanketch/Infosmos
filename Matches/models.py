from django.db import models
from User_Profile.models import Skills, Desires, Askill, Adesire,UserProfile
from django.contrib.auth.models import User
# Create your models here.



class Matches(models.Model):
    user1 =models.ForeignKey(User,related_name='matches_user1')
    user2 =models.ForeignKey(User,related_name='matches_user2')
    offering = models.CharField(db_index=True, max_length=40, null=True)
    recieving =models.CharField(db_index=True, max_length=40, null=True)
    def recieved(self):
        return self.recieving
    
    def giving(self):
        return self.offering
    
    def __unicode__(self):
        return self.user1.username