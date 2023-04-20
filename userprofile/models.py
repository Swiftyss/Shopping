from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='ad')
    last_name = models.CharField(max_length=100, default='ad')
    pix = models.ImageField(upload_to='profile', default='avatar.jpg')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    # dob = models.DateTimeField(auto_now_add=True)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    