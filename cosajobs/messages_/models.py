from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    """This reresents the messahes table sent by each user """
    # the revceiver of the message sent
    receiver=models.ForeignKey(User,on_delete=models.CASCADE)
    
