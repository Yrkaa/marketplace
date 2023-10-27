from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, help_text="Please, enter name with up char")
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.name + str(self.id)