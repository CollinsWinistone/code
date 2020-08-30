from django.contrib import admin
from . models import Job,Qualification,Description,Profile
# Register your models here.

admin.site.register(Job)
admin.site.register(Qualification)
admin.site.register(Description)

admin.site.register(Profile)