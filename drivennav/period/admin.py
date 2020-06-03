from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from drivennav.period.models import Period


@admin.register(Period)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ("date", "year_month", "move_up_down_links")
    prepopulated_fields = {"slug": ("year_month",)}
