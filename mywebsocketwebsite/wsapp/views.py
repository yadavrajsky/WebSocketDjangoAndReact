from django.shortcuts import render


def index(request):
    return render(request, "wsapp/index.html")


def room(request, room_name):
    return render(request, "wsapp/room.html", {"room_name": room_name})