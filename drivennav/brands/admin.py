from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from drivennav.brands.models import Brand


@admin.register(Brand)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ("nome", "move_up_down_links")
    prepopulated_fields = {"slug": ("nome",)}
