from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    category = models.ForeignKey('Service', null=True)
    price = models.CharField(max_length=20, null=False)
