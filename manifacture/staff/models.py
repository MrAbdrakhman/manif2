from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(
        max_length=222
    )
    surname = models.CharField(
        max_length=222
    )
    position = models.CharField(
        max_length=222

    )
    phone = models.CharField(
        max_length=30

    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.name}'