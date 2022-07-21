from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    use_in_migrations = True
    email = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=300)
    username = models.TextField()
    birth = models.TextField()
    gender = models.TextField()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.email}'
