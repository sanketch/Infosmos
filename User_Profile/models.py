from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib


#signals sends out information to other parts of the program
#auth is authentication. I'm not quite sure how it works yet

class Skill(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Desire(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    
class UserProfile(models.Model):
    #This is a start of the user profile page
    user = models.OneToOneField(User, related_name='profile')
    SkillsList = models.CharField( max_length=900, null=True, blank=True)
    DesiresList = models.CharField( max_length=900, null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2,
                                      choices=GENDER_CHOICES,
                                      default='M', null=True)
    desires = models.ManyToManyField(Desire, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    city = models.CharField(db_index=True, max_length=400, blank=True)
    #facebook = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    #basic user fields, more probably for later
    #user = models.ForeignKey(User, unique=True)
    #birth_date = models.DateField(null= True)

    def __unicode__(self):
        return "%s (%s)" % (self.user.username, ",".join([skill.name for skill in self.skills.all()]))

    #for auth
    #class Meta:
    #    db_table = 'db.sqlite3'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
        print "image"
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=200&height=200".format(fb_uid[0].uid)

        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# Create your models here.

#class Skills(models.Model):
#    user =models.ForeignKey(User)
#    skill =models.CharField(db_index=True, max_length=40, null=True)
#    yearxp = models.IntegerField(null=True)
#    description=models.CharField(max_length=400,null=True)
#
#class Desires(models.Model):
#    user=models.ForeignKey(User)
#    wants = models.CharField(db_index=True, max_length=40, null=True)
#    description =models.CharField(max_length=400,null=True)
#
#class Askill(models.Model):
#    userprofile=models.ForeignKey('UserProfile')
#    skill= models.ForeignKey('Skills')
#    date_created=models.DateField()
#
#class Adesire(models.Model):
#    userprofile=models.ForeignKey('UserProfile')
#    desire= models.ForeignKey('Desires')
#    date_created=models.DateField()
