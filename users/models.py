from django.db import models
from datetime import datetime
from conf.models import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    nick_name = models.CharField(max_length=20)

    class Meta:
        ordering = ("-created", )
        db_table = "users"
        verbose_name = "회원들"
        verbose_name_plural = "회원리스트"


    def __str__(self):
        return self.username