from django.db import models
# from django import forms

# Create your models here.
class (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField()

    def __str__(self):
        return self.name

