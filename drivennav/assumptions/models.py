from django.db import models
from drivennav.brands.models import Brand
from drivennav.channel.models import Channel


class Assumptions(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    receivable = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Contas à receber"
    )
    taxes = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Impostos"
    )
    var_sales = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Variáveis de venda"
    )
    other_suppliers = models.DecimalField(
        decimal_places=2, max_digits=15, verbose_name="Demais Fornecedores"
    )
    cogs = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="CMV")
    tvc = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="CTV")
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Assumptions"
        verbose_name_plural = "Assumptions"
