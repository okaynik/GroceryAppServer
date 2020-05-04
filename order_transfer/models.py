from django.db import models

class Order(models.Model):
    ordertext = models.TextField()
    amount = models.TextField()