from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class found_items(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    img = models.ImageField(upload_to='images/',default='images/default.jpg')
    keywords = models.TextField()
    description = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
