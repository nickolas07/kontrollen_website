from django.contrib import admin

from kontrollen.models import Kontrollen, ErstellteKontrollen


# Register your models here.
@admin.register(Kontrollen)
class KontrollenAdmin(admin.ModelAdmin):
    pass


@admin.register(ErstellteKontrollen)
class ErstellteKontrollenAdmin(admin.ModelAdmin):
    pass
