from django.urls import path

from drivennav.base.views import home

app_name = "base"
urlpatterns = [
    path("", home, name="home"),
]
