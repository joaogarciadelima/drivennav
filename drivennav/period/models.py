from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Period(OrderedModel):
    name = models.CharField(max_length=64, verbose_name="Periodo")
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("channels:detail", kwargs={"slug": self.slug})
