from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("/random", views.choose, name="choose"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("wiki/<str:entryname>", views.entry, name="entry")
]
