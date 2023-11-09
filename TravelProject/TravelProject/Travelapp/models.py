from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
class dest(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name