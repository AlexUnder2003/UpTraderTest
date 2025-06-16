# views.py
from django.shortcuts import render
from menu.models import Menu

menus = Menu.objects.all()


def index(request):
    return render(request, "index.html", {"menus": menus})


def about(request):
    return render(request, "about.html", {"menus": menus})


def contact(request):
    return render(request, "contact.html", {"menus": menus})


def team(request):
    return render(request, "team.html", {"menus": menus})


def career(request):
    return render(request, "career.html", {"menus": menus})


def history(request):
    return render(request, "history.html", {"menus": menus})
