from django.db import models
from django.contrib.auth.models import User
from django.conf.global_settings import STATIC_URL
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45,null=True)
    last_name = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='user/')
    city = models.CharField(max_length=45,null=True)

    def __str__(self):
        return self.first_name

    # @property
    # def getImage(self):
    #     if self.image:
    #         return self.image.url
    #     return STATIC_URL+'noimage.jpg'