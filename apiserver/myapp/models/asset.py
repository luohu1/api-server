from django.db import models
from django.utils.translation import gettext_lazy as _


class Asset(models.Model):
    id = models.UUIDField(primary_key=True)
    hostname = models.CharField(_("Hostname"), max_length=128)
    ip = models.CharField(_("IP"), max_length=128)
    port = models.IntegerField(_('Port'), default=22)
