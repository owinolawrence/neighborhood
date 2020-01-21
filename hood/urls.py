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
    url('add_business/',views.add_business,name='add_business'),
    url('business/',views.business,name="business"),
    url('add_post/',views.add_post,name="add_post"),
    url(r'^join_neighbourhood/(?P<hood_id>\d+)$',views.join_neighbourhood,name='join'),
    url(r'^leave_neighbourhood/(?P<hood_id>\d+)$',views.leave_neighbourhood,name='leave'),
    url(r'^s_neighbourhood/(?P<hood_id>\d+)$',views.s_neighbourhood,name='details'),
]