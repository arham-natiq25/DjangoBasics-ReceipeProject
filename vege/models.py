from django.db import models
#django user model ...
from django.contrib.auth.models import User

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name=models.CharField( max_length=50)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe")
    