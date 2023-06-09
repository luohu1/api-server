from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    nickname = models.CharField(_("nickname"), max_length=64)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    password = models.CharField(_("password"), max_length=128)
    email = models.EmailField(_("email address"), blank=True)
    mobile = models.CharField(_("mobile"), max_length=20, blank=True, null=True)
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    created_at = models.DateTimeField(_("create time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    first_name = None
    last_name = None
    date_joined = None

    class Meta:
        db_table = "sys_user"


class Group(models.Model):
    group_name = models.CharField(_("group name"), max_length=64, unique=True)
    group_desc = models.CharField(_("group description"), max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(_("create time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    class Meta:
        db_table = "sys_group"


class Role(models.Model):
    role_name = models.CharField(_("role name"), max_length=64, unique=True)
    role_desc = models.CharField(_("role description"), max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(_("create time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    class Meta:
        db_table = "sys_role"


class Policy(models.Model):
    policy_name = models.CharField(_("policy name"), max_length=64, unique=True)
    policy_desc = models.CharField(_("policy description"), max_length=128, blank=True, null=True)
    policy_spec = models.JSONField(_("policy specification"), max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(_("create time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    class Meta:
        db_table = "sys_policy"
        verbose_name = "Policy"
        verbose_name_plural = "Policies"
