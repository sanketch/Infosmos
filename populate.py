import os
import datetime

#yeah this is one of the most retarded modules ever written
#To run, you have to go to manage.py shell
#and then type execfile('populate.py')
#it automatically creates the admin account
#WARNING: This flushes the database completely

def get_model_fields(model):
    print model._meta.get_all_field_names()
    return

def populate():
    get_model_fields(UserProfile)
    admin= User.objects.create_user('admin', 'a@gmail.com', 'qwerty123')
    joyyie = User.objects.create_user( 'joyyie', 'lolcats@gmail.com', 'e')
    cat = User.objects.create_user( 'cat', 'l2olcats@gmail.com', 'e')
    dog = User.objects.create_user( 'dog', 'lo3lcats@gmail.com', 'ad')
    cow = User.objects.create_user( 'cow', 'lol4cats@gmail.com', 't' )
    pig = User.objects.create_user( 'regibald', 'lolc5ats@gmail.com', '0')
    donkey = User.objects.create_user( 'donkey', 'lolca6ts@gmail.com', 'pop')
    human = User.objects.create_user( 'human', 'lolcat7s@gmail.com', 'pa')
    a = [admin,joyyie,cat,dog,cow,pig,donkey,human]

    for i in a:
        i.first_name= 'jackee'
        i.is_superuser=True
        if i ==admin:
            i.is_staff=True
        else:
            i.is_staff=False
        i.date_joined=datetime.datetime.today()
        i.last_login=datetime.datetime.today()
      
        i.save()
        s = Skills(user=i, skill='tiddlewinks', yearxp=1,description="Yeah bro")
        s.save()
        d = Desires(user=i, wants='fortran', description="Yeah bro")
        d.save()
        r =UserProfile(user=i,city='Detroit')    
        r.save()
        s1 = Askill(skill=s,userprofile=r,date_created=datetime.date(1999,8,2))
        s1.save()
        d1 = Adesire(desire=d,userprofile=r,date_created=datetime.date(1999,8,2))
        d1.save()
if __name__=='__main__':
    print "starting population script"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infosmos.settings')
    from django.contrib.auth.models import User
    from User_Profile.models import UserProfile, Skills, Desires, Askill, Adesire
    from django.core import management
    management.call_command('flush', verbosity=0, interactive=False)
    populate()
    
    
