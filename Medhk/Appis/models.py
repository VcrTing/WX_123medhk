import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Member(models.Model):
    # 微信用户
    openid = models.CharField(max_length=120, null=True, blank=True, verbose_name="OpenId")
    nickName = models.CharField(max_length=30, null=True, blank=True, verbose_name='微信昵称')
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name='国家')
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name='省份')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='城市')
    avatarUrl = models.CharField(max_length=240, verbose_name='微信头像', default='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1556192638273&di=9e48e09e7e73eb477a5cd35be672d912&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F701c1c85751c6cf39cc2e6fdaa4b1f5b6763f9504a7df-QHJpd1_fw658')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name='性别')
    language = models.CharField(max_length=30, null=True, blank=True, verbose_name='语言')

    status = models.BooleanField(verbose_name='是否可用', default=True)
    add_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    class Meta:
        verbose_name = "微信用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nickName:
            return self.nickName
        else:
            return '-空白-'

class Order(models.Model):
    # 订单
    email = models.EmailField(verbose_name='邮箱', null=True)
    sex = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name='性别')
    name = models.CharField(max_length=60, verbose_name='姓名', null=True)
    phone = models.CharField(max_length=30, verbose_name='电话', null=True)
    contry = models.CharField(max_length=240, verbose_name='国籍', null=True)
    birth = models.CharField(max_length=60, verbose_name='出生日期', null=True)
    reserve_time = models.CharField(max_length=60, verbose_name='预约时间', null=True)
    mark = models.CharField(max_length=240, verbose_name='症状', null=True)
    is_complete = models.SmallIntegerField(default=1, verbose_name='预约状态', null=True)

    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, verbose_name='用户')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='数据状态')

    class Meta:
        verbose_name = '预约订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return '-空白-'

class Done(models.Model):
    # 完成记录
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='订单')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, verbose_name='用户')

    add_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='数据状态')

    class Meta:
        verbose_name = '完成记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.member.name:
            return self.member.name
        else:
            return '-空白-'

class Activity(models.Model):
    # 活动消息
    title = models.CharField(max_length=30, verbose_name='标题', null=True)
    content = models.CharField(max_length=120, verbose_name='内容', null=True)
    overdue_time = models.DateTimeField(default=timezone.now, verbose_name='过期时间', null=True)

    add_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='是否启用')

    class Meta:
        verbose_name = '活动消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.title:
            return self.title
        else:
            return '-空白-'