from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    email  = models.EmailField()

    def __str__(self) :
        return self.name