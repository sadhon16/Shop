from django.db import models

class Order(models.Model):
    order = models.CharField(max_length=255)

    def __str__(self):
        return self.order
#class
