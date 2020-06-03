from django.urls import path

from drivennav.period import views

app_name = "period"
urlpatterns = [
    path("<slug:slug>", views.detail, name="detail"),
    # path('aulas/<slug:slug>', views.aula, name='aula'),
    path("", views.indice, name="indice"),
]
