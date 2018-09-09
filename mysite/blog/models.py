from django.db import models

# Create your models here.
class Post(models.Model):
    text=models.CharField(max_length=1000)
    pub_date=models.DateTimeField('date published')
    comment=models.CharField(max_length=1000)
    user_name=models.CharField(max_length=20)
