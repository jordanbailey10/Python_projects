from django.db import models

# Create your models here.
class Class(models.Model):
    Class_Name = models.CharField(max_length=30, default="", blank=True, null=False),
    Course_Number = models.IntegerField(max_length=4, default="", blank=True, null=False),
    Instructor_Name = models.CharField(max_length=30, default="", blank=True, null=False),
    Duration = models.FloatField(max_length=30, default="", blank=True, null=False),

    objects = models.Manager()

    def __str__(self):
        return self. Class_Name