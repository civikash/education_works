from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class Directions(models.Model):
    IT_TECH = 'Информационные технологии'
    MARKETING = 'Маркетинг'
    DESIGN = 'Дизайн'


    PROGRAM_LANG = [
        (IT_TECH, _('Информационные технологиий')),
        (MARKETING, _('Маркетинг')),
        (DESIGN, _('Дизайн')),
    ]

    name = models.CharField(_("Языки программирования"), choices=PROGRAM_LANG, max_length=50)

    def __str__(self):
        return self.name

class Devices(models.Model):
    DESKTOP = 'Десктоп'
    WEB = 'Веб'
    MOBILE = 'Mobile'
    ITEMS = 'Оборудование'
    SMART_ITEMS = 'Умные устройства'


    PROGRAM_LANG = [
        (DESKTOP, _('Десктоп')),
        (WEB, _('Веб')),
        (MOBILE, _('Mobile')),
        (ITEMS, _('Оборудование')),
        (SMART_ITEMS, _('Умные устройства')),
    ]

    name = models.CharField(_("Языки программирования"), choices=PROGRAM_LANG, max_length=50)

    def __str__(self):
        return self.name


class Program(models.Model):
    BASE = 'Базовый'


    PROGRAM_LANG = [
        (BASE, _('Базовый')),
    ]

    name = models.CharField(_("Языки программирования"), choices=PROGRAM_LANG, max_length=50)

    def __str__(self):
        return self.name

class Special(models.Model):
    JUNIOR = 'Junior'
    MIDDLE = 'Middle'
    MIDDLE_PLUS = 'Middle+'

    PROGRAM_LANG = [
        (JUNIOR, _('Junior')),
        (MIDDLE, _('Middle')),
        (MIDDLE_PLUS, _('Middle+')),
    ]

    name = models.CharField(_("Языки программирования"), choices=PROGRAM_LANG, max_length=50)

    def __str__(self):
        return self.name

class LangueProg(models.Model):
    C_PLUS = 'C++'
    C_SHARP = 'C#'
    PYTHON = 'Python'
    JAVA = 'Java'
    JAVA_SCRIPT = 'JavaScript'

    PROGRAM_LANG = [
        (C_PLUS, _('C++')),
        (C_SHARP, _('C#')),
        (PYTHON, _('Python')),
        (JAVA, _('Java')),
        (JAVA_SCRIPT, _('JavaScript')),
    ]

    name = models.CharField(_("Языки программирования"), choices=PROGRAM_LANG, max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    lang = models.ManyToManyField(LangueProg, verbose_name=_("Языки Программирования"))
    title = models.CharField(_("Название курса"), max_length=90)
    description = models.TextField(_("Описание"))
    cost = models.IntegerField(_("Цена"))
    directions = models.ForeignKey(Directions, verbose_name=_("Направления"), on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(Devices, verbose_name=_("Устройства"), on_delete=models.CASCADE, null=True)
    special = models.ForeignKey(Special, verbose_name=_("Уровень"), on_delete=models.CASCADE, null=True)
