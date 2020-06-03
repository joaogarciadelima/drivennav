from django.urls import path

from drivennav.channel import views

app_name = "channels"
urlpatterns = [
    path("<slug:slug>", views.detail, name="detail"),
    # path('aulas/<slug:slug>', views.aula, name='aula'),
    path("", views.indice, name="indice"),
]
