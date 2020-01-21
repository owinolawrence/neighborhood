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

