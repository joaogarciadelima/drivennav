from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from drivennav.channel.models import Channel


@admin.register(Channel)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ("name", "move_up_down_links")
    prepopulated_fields = {"slug": ("name",)}
