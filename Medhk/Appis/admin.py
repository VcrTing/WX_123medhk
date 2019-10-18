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

    list_display = ['nickName', 'country', 'avatar', 'province', 'city', 'gender', 'language', 'add_time', 'status']
    exclude = ['avatarUrl', ]
    fieldsets = (
        ("信息", {
            "fields": (
                'avatar', 'nickName', 'gender'
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
    def color_complete(self, obj):
        if obj.is_complete == 1:
            the_name = '预约中'
            color = 'orange'
        elif obj.is_complete == 2:
            the_name = '已完成'
            color = 'green'
        else:
            the_name = '失效'
            color = 'red'
        return mark_safe(
            '<span style="color: %s;">%s</span>' % (color, the_name)
        )
    color_complete.short_description = '订单状态'

    list_display = ['name', 'phone', 'sex', 'birth', 'reserve_date', 'reserve_time', 'member', 'color_complete', 'add_time', 'status']
    fieldsets = (
        ("资料", {
            "fields": (
                'name', 'sex', 'birth', 'phone'
            )
        }),
        ("信息", {
            "fields": (
                'reserve_date', 'reserve_time', 'is_complete'
            )
        }),
        ("其他", {
            "fields": (
                'member', 'add_time', 'status'
            )
        })
    )
    readonly_fields = ['name', 'sex', 'birth', 'phone', 'member', 'add_time', 'reserve_date', 'reserve_time']
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

"""
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
"""