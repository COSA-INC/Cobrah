from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    """This reresents the messahes table sent by each user """
    # the revceiver's id of the message sent
    message_receiver=models.IntegerField()
    message_sender = models.ForeignKey(User,on_delete=models.CASCADE)
    
