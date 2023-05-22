from django.contrib import admin
from courses.models import Course, LangueProg, Program, Special

@admin.register(Course)
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