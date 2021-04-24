from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("create", views.create),
    path("edit/<int:id>", views.update),
    path("<int:id>", views.show),
    path("delete/<int:id>", views.delete)
]
