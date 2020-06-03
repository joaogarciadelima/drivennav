from django.urls import path

from drivennav.assumptions import views

app_name = "assumptions"
urlpatterns = [
    path("", views.indice, name="indice"),
]
