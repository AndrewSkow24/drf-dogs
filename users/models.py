from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, verbose_name="Почта", unique=True)
    phone = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="Телефон"
    )
    tg_nick = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телеграм-ник"
    )
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"User: {self.email}"
