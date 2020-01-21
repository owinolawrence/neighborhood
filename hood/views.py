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

@login_required
def add_neighbourhood(request):
    current_user = request.user
    post = Posts.objects.all()
    if request.method =='POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            new_neigh = form.save(commit=False)
            new_neigh.admin = current_user
            new_neigh.occupants = 0
            new_neigh.save()
            return redirect('home')
        
    else:
        form = NeighbourhoodForm()

    return render(request,'main/neighbourhoodform.html',{"form":form,'post':post})



@login_required
def add_business(request):
    current_user = request.user
    post = Posts.objects.all()
    if request.method == 'POST':
        form = bForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.user_posted = request.user
            post.save()
            return redirect('home')
    else:
        form = PostsForm()
   

    return render(request,'main/businessform.html',{'post':post})


@login_required
def business(request):
  post = Posts.objects.all()
  return render(request,'main/business.html',{'post':post})


@login_required
def add_post(request):
  post = Posts.objects.all()
  return render(request,"main/post_form.html",{'post':post})

@login_required
def join_neighbourhood(request,hood_id):
    hood= get_object_or_404(Neighbourhood,id=hood_id)
    hood.occupants = hood.occupants + 1
    hood.save()
  

    user = request.user
    profile = get_object_or_404(Profile,name=user)

    profile.neighbourhood = hood
    profile.save()
    return render(request,'main/index.html', {"profile":profile,'hood':hood})

def s_neighbourhood(request,hood_id):
  post = Posts.objects.all()
  hood_details = get_object_or_404(Neighbourhood, id=hood_id)
  return render (request,'main/detailhood.html',{"hood_details":hood_details, 'post':post})

@login_required
def leave_neighbourhood(request,hood_id):

    hood= get_object_or_404(Neighbourhood,id=hood_id)
    hood.occupants = hood.occupants - 1
    hood.save()
  

    user = request.user
    profile = get_object_or_404(Profile,name=user)

    profile.neighbourhood = None
    profile.save()

    return redirect('home')

@login_required
def add_post(request):
    post = Posts.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.user_posted = request.user
            post.save()
            return redirect('home')
    else:
        form = PostsForm()
    return render(request, 'post_form.html', {'form': form,'post':post})