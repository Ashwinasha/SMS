# students/models.py
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=4, unique=True, verbose_name='Student ID')
    name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.student_id
    
    class Meta:
        app_label = 'students'
