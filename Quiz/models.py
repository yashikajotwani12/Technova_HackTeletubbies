from django.db import models

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length= 50)
    description = models.TextField(max_length=5000)
    video= models.CharField(max_length=200)
    image= models.CharField(max_length=100)
    quiz = models.CharField(max_length=100)

    def __str__(self):
        return self.name
