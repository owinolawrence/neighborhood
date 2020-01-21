from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from . import forms
from .models import  Profile,Posts,Neighbourhood
from .forms import RegisterForm, ProfileForm,PostsForm,NeighbourhoodForm,UpdateProfileForm,UpdateUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

@login_required
def home(request):
    user = request.user
    neigh = Neighbourhood.objects.all()
    post = Posts.objects.all()
    return render(request,'main/index.html', {'user':user,"neigh":neigh,'post':post})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            input_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=input_password)
            login(request, user)
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else :
        form = RegisterForm()
    return render (request, 'registration/registration_form.html', {'form':form})

@login_required
def profile(request):
    post = Posts.objects.all()
    current_user = request.user
    profile = get_object_or_404(Profile, name=current_user)
    return render(request, 'main/profile.html',{"current_user":current_user,"profile":profile,"post":post})

@login_required
def update_profile(request):
  post = Posts.objects.all()
  if request.method == 'POST':
    user_form = UpdateUser(request.POST,instance=request.user)
    profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUser(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile) 
  forms = {
    'user_form':user_form,
    'profile_form':profile_form,
    'post':post
  }
  return render(request,'main/edit_profile.html',forms)

