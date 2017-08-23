from django.contrib import admin
from .models import Curator, CurTime
# Register your models here.


@admin.register(Curator)
class CuratorAdmin (admin.ModelAdmin):
    pass


@admin.register(CurTime)
class CurTimeAdmin (admin.ModelAdmin):
    pass
