from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
import uuid
from django.utils.translation import gettext_lazy as _
from account.managers import AccountManager
import pytz


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name


class Account(AbstractUser):
    M = 'Мужчина'
    F = 'Женщина'

    GENDER = [
        (M, _('Мужчина')),
        (F, _('Женщина')),
    ]

    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    username = None
    email = models.EmailField(_('Адрес электронной почты'), unique=True)
    patronymic = models.CharField(_("Отчество"), max_length=60, null=True, blank=True)
    birthday = models.DateField(_("Дата рождения"), auto_now=False, auto_now_add=False, null=True, blank=True)
    time_zone_choices = [(tz, tz) for tz in pytz.all_timezones]
    time = models.CharField(_("Часовой пояс"), max_length=50, choices=time_zone_choices, null=True, blank=True)
    myself = models.TextField(_("О себе")) 
    hobby = models.TextField(_("Интересы"))
    number = models.IntegerField(_("Телефон"), null=True, blank=True)
    country = models.CharField(_("Страна"), max_length=50, null=True, blank=True)
    city = models.CharField(_("Город"), max_length=90, null=True, blank=True)
    gender = models.CharField(_("Пол"), choices=GENDER, max_length=50, null=True, blank=True)
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    roles = models.ManyToManyField(
        Role,
        verbose_name=_('roles'),
        blank=True,
        related_name='accounts'
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='account_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='account_user_permissions'
    )