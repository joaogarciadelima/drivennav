from django.shortcuts import render

#
# # Create your views here.
from drivennav.period import facade


def indice(request):
    ctx = {"channels": facade.list_periods_ordeneds()}
    return render(request, "modulos/indice.html", ctx)


def detail(request, slug):
    channel = facade.find_period(slug)
    # aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, "modulos/modulo_detalhe.html", {"channel": channel})


# def aula(request, slug):
#     aula = facade.encontrar_aula(slug)
#     return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
