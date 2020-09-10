from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.page, name="new_page"),
    path("wiki/<str:name>/",views.index,name = "index"),




]
