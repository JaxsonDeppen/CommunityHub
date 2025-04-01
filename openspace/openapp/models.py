from django.db import models

# Create your models here.
class Events(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=400)
    Location = models.CharField(max_length=300)
    Date = models.DateTimeField(auto_now_add=True)

