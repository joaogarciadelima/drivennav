from django.shortcuts import render

from .forms import AssumptionsForm


def indice(request):
    if request.method == "POST":
        form = AssumptionsForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "assumptions/assumptions_detail.html", {"form": form})
    else:
        form = AssumptionsForm()
    return render(request, "assumptions/assumptions_detail.html", {"form": form})
