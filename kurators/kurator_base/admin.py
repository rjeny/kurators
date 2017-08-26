from django.contrib import admin
from .models import Curator, CurTime, StudentGroup
# Register your models here.


@admin.register(Curator)
class CuratorAdmin (admin.ModelAdmin):
    pass


@admin.register(CurTime)
class CurTimeAdmin (admin.ModelAdmin):
    pass


@admin.register(StudentGroup)
class GroupAdmin (admin.ModelAdmin):
    pass
