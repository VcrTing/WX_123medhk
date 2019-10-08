from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db import models as djmodel
from django.contrib.auth.admin import UserAdmin

from . import models
from Medhk.settings import ADMIN_CONF

admin.site.site_title = ADMIN_CONF['admin_title']
admin.site.site_header = ADMIN_CONF['admin_header']

# Register your models here.
@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):

    avatar = djmodel.ImageField()
    def avatar(self, obj):
        return mark_safe('<img src="%s" width="28" height="28" style="border-radius:100px"/>' % (obj.avatarUrl,))
    avatar.allow_tags = True
    avatar.short_description = '微信头像'

    list_display = ['nickName', 'country', 'province', 'city', 'gender', 'language', 'add_time', 'status']
    exclude = ['avatarUrl', ]
    fieldsets = (
        ("信息", {
            "fields": (
                'nickName', 'gender'
            )
        }),
        ("地址", {
            "fields": (
                'country', 'province', 'city'
            )
        }),
        ("其他", {
            "fields": (
                'language', 'add_time', 'status'
            )
        })
    )
    readonly_fields = list_display
    search_fields = ['nickName', 'country', 'province']
    list_filter = ['gender', 'status']
    date_hierarchy = 'add_time'
    empty_value_display = ADMIN_CONF['empty_value_display']
    
    def get_ordering(self, request):
        return ['-add_time', ]

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'sex', 'name', 'contry', 'birth', 'reserve_time', 'member', 'is_complete', 'add_time', 'status']
    fieldsets = (
        ("资料", {
            "fields": (
                'name', 'sex', 'contry', 'birth', 'phone', 'email'
            )
        }),
        ("信息", {
            "fields": (
                'reserve_time', 'mark', 'is_complete'
            )
        }),
        ("其他", {
            "fields": (
                'member', 'add_time', 'status'
            )
        })
    )

    search_fields = ['name', 'email', 'contry']
    list_filter = ['sex', 'status']
    date_hierarchy = 'add_time'
    empty_value_display = ADMIN_CONF['empty_value_display']

@admin.register(models.Done)
class DoneAdmin(admin.ModelAdmin):
    list_display = ['order', 'member', 'add_time', 'status']
    fieldsets = (
        ("记录主体", {
            "fields": (
                'order', 'member'
            )
        }),
        ("其他", {
            "fields": (
                'add_time', 'status'
            )
        })
    )

    search_fields = ['order', 'member']
    list_filter = ['status', ]
    date_hierarchy = 'add_time'
    empty_value_display = ADMIN_CONF['empty_value_display']

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'overdue_time', 'add_time', 'status']
    fieldsets = (
        ("活动内容", {
            "fields": (
                'title', 'content', 'overdue_time'
            )
        }),
        ("其他", {
            "fields": (
                'add_time', 'status'
            )
        })
    )

    search_fields = ['title', ]
    list_filter = ['status', ]
    date_hierarchy = 'add_time'
    empty_value_display = ADMIN_CONF['empty_value_display']