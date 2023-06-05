from django.db import models
from django.utils.translation import gettext_lazy as _


class DBInstance(models.Model):
    class ProviderChoices(models.IntegerChoices):
        SELFHOST = 0, _('Self-Host')
        ALIYUN = 1, _('Aliyun')

    class EngineChoices(models.IntegerChoices):
        MYSQL = 0, _('MySQL')
        POLARDB = 1, _('PolarDB')
        MARIADB = 2, _('MariaDB')
        SQLSERVER = 3, _('SQLServer')
        POSTGRESQL = 4, _('PostgreSQL')

    class TypeChoices(models.IntegerChoices):
        Primary = 0, _('Primary')
        Readonly = 1, _('Readonly')
        Guard = 2, _('Guard')
        Temp = 3, _('Temp')

    class StatusChoices(models.IntegerChoices):
        RUNNING = 0, _('RUNNING')
        STOPPED = 1, _('STOPPED')
        OFFLINE = 2, _('OFFLINE')

    name = models.CharField(max_length=255, unique=True, verbose_name=_('实例名称'))
    provider = models.IntegerField(choices=ProviderChoices.choices, default=ProviderChoices.ALIYUN, verbose_name=_('提供商'))
    instance_id = models.CharField(max_length=128, blank=True, null=True)
    instance_class = models.CharField(max_length=128, blank=True, null=True)
    instance_type = models.IntegerField(choices=TypeChoices.choices, default=TypeChoices.Primary, verbose_name=_('实例类型'))
    engine = models.IntegerField(choices=EngineChoices.choices, default=EngineChoices.MYSQL, verbose_name=_('数据库引擎'))
    version = models.CharField(max_length=32, blank=True, default='', verbose_name=_('数据库版本'))
    host = models.CharField(max_length=255, blank=True, verbose_name=_('数据库链接'))
    port = models.IntegerField(default=3306, verbose_name=_('数据库端口'))
    username = models.CharField(max_length=128, blank=True, verbose_name=_('超管账号'))
    password = models.CharField(max_length=128, blank=True, verbose_name=_('超管密码'))
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.OFFLINE, verbose_name=_('服务状态'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("修改时间"))

    class Meta:
        verbose_name_plural = verbose_name = '数据库实例实体表'
        ordering = ['-pk']

    def __str__(self) -> str:
        return self.name


class Database(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('数据库名称'))
    desc = models.TextField(blank=True, default='', verbose_name=_('描述信息'))
    charset = models.CharField(max_length=128, blank=True, null=True)
    db_instance = models.ForeignKey(to='DBInstance', related_name='databases', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("修改时间"))

    class Meta:
        verbose_name_plural = verbose_name = '数据库实体表'
        ordering = ['-pk']

    def __str__(self) -> str:
        return self.name
