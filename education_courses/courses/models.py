from django.db import models
from account.models import Account
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
    image = models.ImageField(_("Изображение"), upload_to='static/img/directions_images/')

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
    
class Package(models.Model):
    BASE = 'Базовый'
    MASTER = 'Мастер'
    PRO = 'Про'

    PROGRAM_PACKAGE = [
        (BASE, _('Базовый')),
        (MASTER, _('Мастер')),
        (PRO, _('Про')),
    ]

    
    DIPLOM_1 = 'В конце обучения'
    DIPLOM_2 = '12 месяцев'

    DIPLOMS = [
        (DIPLOM_1 , _('В конце обучения')),
        (DIPLOM_2, _('12 месяцев')),
    ]

    TIME_1 = '12 месяцев'
    TIME_2 = '24 месяцев'
    TIME_3 = '36 месяцев'

    TIMES = [
        (TIME_1 , _('12 месяцев')),
        (TIME_2, _('24 месяцев')),
        (TIME_3, _('36 месяцев')),
    ]

    PRICE_1 = '3510'
    PRICE_2 = '4052'
    PRICE_3 = '5921'

    PRICES = [
        (PRICE_1 , _('3510')),
        (PRICE_2, _('4052')),
        (PRICE_3, _('5921')),
    ]

    name = models.CharField(_("Пакет"), choices=PROGRAM_PACKAGE, max_length=50)
    level = models.ForeignKey(Special, verbose_name=_("Знания на выходе"), on_delete=models.CASCADE, null=True)
    diplom = models.CharField(_("Пакет"), choices=DIPLOMS, max_length=90, null=True)
    time = models.CharField(_("Срок обучения"), choices=TIMES, max_length=90, null=True)
    price = models.CharField(_("Цена в месяц"), choices=PRICES, max_length=90, null=True)

    def __str__(self):
        return self.name
    
class Temp(models.Model):
    STANDART = 'Стандартный'
    INTENSIVE = 'Интенсивный'
    SLOW = 'Замедленный'

    PROGRAM_TEMP = [
        (STANDART, _('Стандартный')),
        (INTENSIVE, _('Интенсивный')),
        (SLOW, _('Замедленный')),
    ]

    PRICE_1 = 'Бесплатно'
    PRICE_2 = '1621'

    PRICES = [
        (PRICE_1, _('Бесплатно')),
        (PRICE_2, _('1621'))
    ]

    name = models.CharField(_("Темп"), choices=PROGRAM_TEMP, max_length=50)
    price = models.CharField(_("Цена в месяц"), choices=PRICES, max_length=90, null=True)

    def __str__(self):
        return self.name
    

class Option(models.Model):
    INDIVID = 'Индивидуальные занятия'
    DIPLOM = 'Диплом установленного образца'
    GARANT = 'Гарантия трудоустройства'
    PROF = 'Профориентация'

    PROGRAM_OPTION = [
        (INDIVID, _('Индивидуальные занятия')),
        (DIPLOM, _('Диплом установленного образца')),
        (GARANT, _('Гарантия трудоустройства')),
        (PROF, _('Профориентация'))
    ]

    PRICE_1 = '12500'
    PRICE_2 = '30000'
    PRICE_3 = '25000'

    PRICES = [
        (PRICE_1, _('12500')),
        (PRICE_2, _('30000')),
        (PRICE_3, _('25000'))
    ]

    name = models.CharField(_("Опция"), choices=PROGRAM_OPTION, max_length=150)
    price = models.CharField(_("Цена в месяц"), choices=PRICES, max_length=90, null=True)

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
    
class Target(models.Model):
    name = models.CharField(_("Цели"), max_length=90)

    def __str__(self):
        return self.name
    

class TypeEducation(models.Model):
    name = models.CharField(_("Тип обучения"), max_length=90)
    description = models.TextField(_("Описание"))

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


class Order(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(Account, verbose_name=_("Пользователь"), on_delete=models.CASCADE, null=False)
    directions = models.ForeignKey(Directions, verbose_name=_("Направления"), on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, verbose_name=_("Пакет"), on_delete=models.CASCADE, null=True)
    temp = models.ForeignKey(Temp, verbose_name=_("Темп обучения"), on_delete=models.CASCADE, null=True)
    name = models.CharField(_("Имя фамилия"), max_length=250)
    email = models.CharField(_("Email"), max_length=15)
    type_education = models.ForeignKey(TypeEducation, verbose_name=_("Тип обучения"), on_delete=models.CASCADE, null=True)
    option = models.ManyToManyField(Option, verbose_name=_("Опции"))
    target = models.ManyToManyField(Target, verbose_name=_("Цели"))
    phone_number = models.CharField(max_length=13, unique=True)
    value = models.FloatField(_("Сумма"), null=True)

    def save(self, *args, **kwargs):
        # Проверка и обработка номера телефона перед сохранением
        if not self.phone_number.startswith('+7'):
            self.phone_number = '+7' + self.phone_number[-10:]
        super().save(*args, **kwargs)