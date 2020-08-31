

from django.db import models
from jobs.models import Job

from django.contrib.auth.models import User


class Suggestions(models.Model):
    """ Contains suggestions for a particular user"""
  
    job_suggestion=models.ForeignKey(Job,on_delete=models.CASCADE) # the job suggested for a particular user
    user=models.ForeignKey(User,on_delete=models.CASCADE) # the user to whom the job is suggested to
    
    
    
    