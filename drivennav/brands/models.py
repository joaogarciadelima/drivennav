from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Brand(OrderedModel):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("brands:detail", kwargs={"slug": self.slug})
