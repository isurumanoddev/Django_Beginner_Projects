from django.shortcuts import render

from base.models import Room, Message, Topic


# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_comments = Message.objects.all()
    topics = Topic.objects.all()
    context = {"room": room, "room_comments": room_comments, "topics": topics}
    return render(request, "room.html", context)


def create_room(request):
    if request.method == "POST":
        form =
    context = {"rooms": rooms}
    return render(request, "home.html", context)
