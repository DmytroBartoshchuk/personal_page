from django.db import models


class CustomLink(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=500)

