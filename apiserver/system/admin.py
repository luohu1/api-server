from django.contrib import admin

from . import models


class BaseAdmin(admin.ModelAdmin):
    actions_on_top = False
    actions_on_bottom = True

    def __init__(self, model, admin_site) -> None:
        self.list_display = [field.name for field in model._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]
        super().__init__(model, admin_site)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('username', 'is_active')

    def __init__(self, model, admin_site) -> None:
        self.list_display = [field.name for field in model._meta.fields if field.name not in ['password', 'created_at', 'updated_at']]
        super().__init__(model, admin_site)


admin.site.register([models.Group, models.Role], BaseAdmin)
