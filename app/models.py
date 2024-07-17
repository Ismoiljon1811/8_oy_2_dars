from django.db import models

class Car(models.Model):
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 80)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name