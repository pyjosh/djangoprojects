from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTime('date published')
    likes = model.IntegerField()