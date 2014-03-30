from django import forms
from User_Profile.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name', 'email', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('city',)

		
