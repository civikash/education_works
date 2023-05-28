from django.contrib import admin
from courses.models import Course, Package, Temp, Option, LangueProg, Order, Program, Special, Directions, Devices

@admin.register(Course)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Package)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Temp)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(LangueProg)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Program)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Special)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Devices)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Directions)
class AccountAdmin(admin.ModelAdmin):
    pass