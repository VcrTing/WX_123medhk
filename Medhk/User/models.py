import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class UserProfile(AbstractUser):
    # 员工
    nickName = models.CharField(max_length=20, null=True, blank=True, verbose_name='员工真实姓名')
    bith = models.DateField(null=True, blank=True, verbose_name='出生年月')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name='性别')
    is_staff = models.BooleanField(default=True, verbose_name='职员状态', help_text='指明用户是否可以登录到这个管理站点。')
    is_superuser = models.BooleanField(default=False, verbose_name='是否超级用户', help_text='无视权限认证，一键拥有超级权限。')
    password = models.CharField(max_length=240, verbose_name='登录密码')

    status = models.BooleanField(verbose_name='账号是否可用', default=True)
    add_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.email:
            return self.email
        else:
            return '-空白-'
