from django.db import models

def start(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
