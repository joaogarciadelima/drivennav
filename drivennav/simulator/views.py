from django.shortcuts import render

from .forms import SimulatorForm


def indice(request):
    if request.method == "POST":
        form = SimulatorForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "simulator/simulator_detail.html", {"form": form})
    else:
        form = SimulatorForm()
    return render(request, "simulator/simulator_detail.html", {"form": form})
