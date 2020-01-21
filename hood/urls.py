from django.conf.urls import url 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url('^$',views.home, name='home'),
    url('signup/', auth_views.LoginView.as_view(template_name='registration/registration_form.html'),name= 'signup'),
    url('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name= 'login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'),
    url('update/',views.update_profile,name='update_profile'),
    url('add_neighbourhood/',views.add_neighbourhood,name='add_neighbourhood'),
        
]