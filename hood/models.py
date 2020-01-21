from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100,default='MyNeighbourhood',null=True)
    location = models.CharField(max_length=100,null=True)
    occupants= models.IntegerField(blank=True,default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighbourhood_image =models.ImageField(upload_to='neighbourhoods/')

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)


class Posts(models.Model):

    
    post_content = models.CharField(max_length=100,null=True)
    user_posted = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email = models.EmailField()


class Profile(models.Model):

    profile_image = models.ImageField(upload_to='avatars/',null=True)
    bio = models.CharField(max_length=100,null=True)
    name = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile',null=True)
    neighbourhood =models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)
    email = models.EmailField()
    age = models.IntegerField(null=True)

class Business(models.Model):

    business_image = models.ImageField(upload_to='avatars/',null=True)
    about = models.CharField(max_length=100,null=True)
    name =  models.CharField(max_length=100)
    neighbourhood =models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)
    email = models.EmailField()
    contacts = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


@receiver(post_save,sender=User)
def default_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(name=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return self.name