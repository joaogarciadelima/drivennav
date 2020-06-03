from django.urls import path

from drivennav.data import views

app_name = "data"
urlpatterns = [
    path("", views.indice, name="indice"),
]
