from django.urls import path

from drivennav.brands import views

app_name = "brands"
urlpatterns = [
    path("<slug:slug>", views.detail, name="detail"),
    # path('aulas/<slug:slug>', views.aula, name='aula'),
    path("", views.indice, name="indice"),
]
