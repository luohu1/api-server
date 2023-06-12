from django.db import models
from django.utils.translation import gettext_lazy as _


class App(models.Model):
    app_name = models.CharField(_("app name"), max_length=128)

    class Meta:
        ordering = ['id', ]

    def __str__(self) -> str:
        return self.app_name
