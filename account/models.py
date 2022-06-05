#Library Import
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
#Local Import
from .manager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='ایمیل کاربر',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, verbose_name='نام کاربری')
    is_active = models.BooleanField(default=True, verbose_name='مجوز ورود به سایت؟')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین سایت؟')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin