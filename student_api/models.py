from operator import mod
from tkinter import CASCADE
from django.db import models

import student_api

# Create your models here.

class StudentDetails(models.Model):
    
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    guardian_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name

class ScoreList(models.Model):
    
    full_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    score = models.FloatField()
    
    def __str__(self):
        return self.full_name



