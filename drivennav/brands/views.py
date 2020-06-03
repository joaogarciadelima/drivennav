from django.shortcuts import render

#
# # Create your views here.
from drivennav.brands import facade


def indice(request):
    ctx = {"brands": facade.list_brands_ordeneds()}
    return render(request, "modulos/indice.html", ctx)


def detail(request, slug):
    brand = facade.find_brand(slug)
    # aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, "modulos/modulo_detalhe.html", {"brand": brand})


# def aula(request, slug):
#     aula = facade.encontrar_aula(slug)
#     return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
