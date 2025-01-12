from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    file = models.FileField(null=True, blank=True, upload_to='ticket_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return self.subject
    

class Message(models.Model):
    ticket = models.ForeignKey(Ticket, models.CASCADE, related_name='messages')
    user_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_message
