from django.shortcuts import render

from base.form import RoomForm
from base.models import Room, Message, Topic


# Create your views here.


def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {"rooms": rooms,"topics":topics}
    return render(request, "home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {"room": room}
    return render(request, "room.html", context)


def create_room(request):
    form = RoomForm()
    # if request.method == "POST":
    print(form.)

    context = {"form": form}
    return render(request, "room_form.html", context)
