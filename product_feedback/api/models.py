from django.db import models


class ProductRequests(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class CurrentUser(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
