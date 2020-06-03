from django.db import models
# from django.urls import reverse
from drivennav.brands.models import Brand
from drivennav.channel.models import Channel
from drivennav.period.models import Period


class Data(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    initial_inventory = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Estoque inicial"
    )
    sales = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="Vendas")
    discount = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Desconto %"
    )
    purchase = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Purchase"
    )
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data"
