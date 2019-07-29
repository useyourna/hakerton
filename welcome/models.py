from django.db import models

class Profile(models.Model):
    image = models.ImageField(upload_to="images/")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
  
    
    
# Create your models here.
