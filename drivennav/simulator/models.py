from django.db import models
# from django.urls import reverse
from drivennav.brands.models import Brand
from drivennav.channel.models import Channel
from drivennav.period.models import Period


class Simulator(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marca")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name="Canal")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name="Mês/Ano")
    sales_perform = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Sales Perform %"
    )
    discount = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Desconto %"
    )
    purchase = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Purchase"
    )
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Simulator"
        verbose_name_plural = "Simulators"
