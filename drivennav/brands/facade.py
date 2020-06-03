from typing import List
from drivennav.brands.models import Brand


def list_brands_ordeneds() -> List[Brand]:
    """
    Lista de módulos ordenados por títulos
    :return:
    """
    return list(Brand.objects.order_by("order").all())


def find_brand(slug: str) -> Brand:
    return Brand.objects.get(slug=slug)


# def encontrar_aula(slug: str) -> Aula:
#     return Aula.objects.select_related('modulo').get(slug=slug)


# def listar_modulos_com_aulas():
#     aulas_ordenadas = Aula.objects.order_by('order')
#     return Modulo.objects.order_by('order').prefetch_related(
#         Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
#     ).all()
