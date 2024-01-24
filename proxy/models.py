from django.contrib.auth.models import User
from django.db import models


class UserSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    site_url = models.URLField()

    def __str__(self):
        return self.site_name

