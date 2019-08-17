from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=10)