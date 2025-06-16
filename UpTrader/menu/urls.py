# menu_example/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("about/team/", views.team, name="team"),
    path("contact/", views.contact, name="contact"),
    path("about/team/careers/", views.career, name="carreer"),
    path("about/history/", views.history, name="history"),
]
