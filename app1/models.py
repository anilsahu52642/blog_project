from django.db import models
from django.contrib.auth.models import User


class blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    title=models.CharField(max_length=64,default='Title')
    content=models.CharField(max_length=64,default='content')
    photo=models.ImageField(upload_to='image')

