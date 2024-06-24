from django.db import models


class CurrentUser(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
