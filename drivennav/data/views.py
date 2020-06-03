from django.shortcuts import render
from .forms import DataForm


def indice(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "data/data_detail.html", {"form": form})
    else:
        form = DataForm()
    return render(request, "data/data_detail.html", {"form": form})
