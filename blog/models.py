from django.db import models
from django.db.models import TextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = TextField()
    image = models.ImageField(upload_to='images/')
