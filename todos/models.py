from django.db import models
class Items(models.Model):
    name=models.TextField()
    cost=models.TextField()
    quantity=models.TextField()
    description=models.TextField(default='this is cool!')
    



# Create your models here.
