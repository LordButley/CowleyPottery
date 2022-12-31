from django.db import models

class Commission(models.Model):
    """
    A model for storing commission data
    """

    name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    details = models.TextField(max_length=600, blank=False, null=False)
    