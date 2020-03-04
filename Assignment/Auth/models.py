from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers.usermanager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # add additional fields in here
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True,blank=False)
    phone = models.CharField(null=True, blank=True,max_length=50)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'),default=True)
    last_activity = models.DateTimeField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(blank=True,null=True)

    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name']
    def __str__(self):
        return self.email
