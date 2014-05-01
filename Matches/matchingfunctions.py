'''
Created on Apr 8, 2014

@author: Mr. Awesomepants
'''
from User_Profile.models import UserProfile, Skills, Desires
from django.contrib.auth.models import User
from Matches.models import Matches
def match_user(person):
    '''This function takes as inpudt user class'''
    
    for x in Desires.objects.filter(user__exact = person):
        r=Matches(user1=person)
        for y in Skills.objects.filter(skill__exact= x.wants):
                r.user2 = y.user
                r.offering = y.skill
                r.recieving =x.desire
                r.save
        
    
    
    






