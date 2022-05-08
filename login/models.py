from django.db import models


class UserInfo(models.Model):
    mid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    follower = models.IntegerField(blank=True, null=True)
    vip = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class LoginInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='账号名称')
    password = models.CharField(max_length=20, verbose_name='用户密码')
