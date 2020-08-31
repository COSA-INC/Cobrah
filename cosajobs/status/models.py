from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    """This models stores each user status on a particular job needs"""
    status =models.CharField(max_length=25)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return "status for "+self.user.username 
    
    
