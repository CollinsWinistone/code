from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    """This models the user profile"""
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='profile_pics',default='profile_pics/test.jpg')
    
    def __str__(self):
        return self.user.username
    
    
    
class Job(models.Model):
    
    """This models the job database"""
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    job_name=models.CharField(max_length=100)
    job_image = models.ImageField(upload_to='jobs_pictures',default='profile_pics/test.jpg')
    
    
    def __str__(self):
        return self.job_name
    
    
class Qualification(models.Model):
    """This models the qualifications for a particular job"""
    job =models.ForeignKey(Job,on_delete=models.CASCADE)
    jQual =models.TextField()
    
    def __str__(self):
        return self.jQual
    
class Description(models.Model):
    """This models the job description"""
    job = models.ForeignKey(Job,models.CASCADE)
    job_description =models.TextField()
    
    def __str__(self):
        return self.job_description
    

    
   
    
