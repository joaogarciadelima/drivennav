from typing import List

# from django.db.models import Prefetch

from drivennav.period.models import Period


def list_periods_ordeneds() -> List[Period]:
    """
    Lista de módulos ordenados por títulos
    :return:
    """
    return list(Period.objects.order_by("order").all())


def find_period(slug: str) -> Period:
    return Period.objects.get(slug=slug)


# def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
#     return list(modulo.aula_set.order_by('order').all())


# def encontrar_aula(slug: str) -> Aula:
#     return Aula.objects.select_related('modulo').get(slug=slug)


# def listar_modulos_com_aulas():
#     aulas_ordenadas = Aula.objects.order_by('order')
#     return Modulo.objects.order_by('order').prefetch_related(
#         Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
#     ).all()
