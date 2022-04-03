from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.accounts.managers import PetstagramUserManager

class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USER_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USER_MAX_LENGTH,
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()
