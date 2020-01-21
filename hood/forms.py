from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Posts,Neighbourhood,Business
class RegisterForm(UserCreationForm):
    fullname = forms.CharField(max_length=150,required=False,help_text='Optional.')
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta :
        model = User
        fields =('username','fullname','email','password1','password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=['user_posted']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['occupants','admin']

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_image','bio']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class BusinessForm(forms.ModelForm):
  
  class Meta:
    model = Business
    exclude = []