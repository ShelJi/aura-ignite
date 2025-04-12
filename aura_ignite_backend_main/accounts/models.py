from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    balance = models.IntegerField(_("Balance"), default=0)
    total_gain = models.IntegerField(_("Total Gain"), default=0)
    total_loss = models.IntegerField(_("Total Loss"), default=0)
    total_needs_to_pay = models.IntegerField(_("Total Need to Pay"), default=0)
    total_needs_to_get = models.IntegerField(_("Total Need to Get"), default=0)
    total_pending = models.IntegerField(_("Total Pending"), default=0)
    
    def __str__(self):
        return self.username