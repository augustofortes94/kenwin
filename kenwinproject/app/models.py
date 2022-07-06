from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, null=True, blank=True, default=None)
    enterprice = models.CharField(max_length=50, null=True, blank=True, default=None)
    number = models.CharField(max_length=50, null=True, blank=True, default=None)
    email = models.EmailField(max_length=50, null=True, blank=True, default=None)
    address = models.CharField(max_length=50, null=True, blank=True, default=None)
