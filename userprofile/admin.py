from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =['id', 'first_name', 'last_name', 'pix', 'email', 'address', 'dob', 'nationality', 'gender', 'state']
admin.site.register(Profile, ProfileAdmin)