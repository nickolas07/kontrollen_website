from django.contrib import admin
from aufgaben.models import Themen


# Register your models here.
@admin.register(Themen)
class ThemenAdmin(admin.ModelAdmin):
    pass
