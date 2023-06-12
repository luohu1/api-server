from django.db import models
from django.utils.translation import gettext_lazy as _

from . import App


class Asset(models.Model):
    hostname = models.CharField(_("Hostname"), max_length=128)
    ip = models.CharField(_("IP"), max_length=128)
    port = models.IntegerField(_('Port'), default=22)

    apps = models.ManyToManyField(App)

    class Meta:
        ordering = ['id', ]
