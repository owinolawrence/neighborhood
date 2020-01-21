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


