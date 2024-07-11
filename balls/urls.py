from django.urls import path
from . import views

urlpatterns = [
    path("display/", views.display_ball),
    path("display/report", views.get_report),
]