from django.db import models

# Create your models here.
class To_Do(models.Model):
    data = models.CharField(max_length=150, default='')
    timeStamp= models.DateTimeField(blank=True)

