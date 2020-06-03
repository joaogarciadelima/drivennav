from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Period(OrderedModel):
    date = models.DateField(verbose_name="Data")
    year_month = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.year_month

    def get_absolute_url(self):
        return reverse("channels:detail", kwargs={"slug": self.slug})
