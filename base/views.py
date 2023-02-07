from django.shortcuts import render, redirect

from base.form import RoomForm
from base.models import Room, Message, Topic


# Create your views here.


def home(request):
    if request.GET.get("q") is not None:
        q = request.GET.get("q")
        print(q)
    else:
        q = ""
    rooms= Room.objects.filter(topic__name__contains=q)
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics}
    return render(request, "home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {"room": room}
    return render(request, "room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"room": room}
    return render(request, "delete.html", context)
