from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(null=True, blank=True)
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
