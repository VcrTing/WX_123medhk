from django.contrib import admin
from django.db import models as djmodel
from django.contrib.auth.admin import UserAdmin

from . import models
from Medhk.settings import ADMIN_CONF

admin.site.site_title = ADMIN_CONF['admin_title']
admin.site.site_header = ADMIN_CONF['admin_header']

# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'nickName', 'bith', 'phone', 'email', 'gender', 'status']
    search_fields = ['phone', 'email']
    list_filter = ['gender', 'status']
    readonly_fields = ['last_login']
    exclude = ['id']
    fieldsets = (
        ("账号信息", {
            "fields": (
                'username', 'email', 'password'
            ),
        }),
        ("权限相关", {
            "fields": (
                'is_staff', 'is_active', 'groups'
            ),
        }),
        ("个人资料", {
            "fields": (
                'nickName', 'bith', 'phone', 'gender'
            ),
        }),
        ("其他", {
            "fields": (
                'last_login', 'date_joined'
            ),
        }),
    )
    list_per_page = 50
    empty_value_display = ADMIN_CONF['empty_value_display']
