from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
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
    rooms = Room.objects.filter(topic__name__contains=q)
    topics = Topic.objects.all()
    comments = Message.objects.filter(room__topic__name__icontains=q)
    context = {"rooms": rooms, "topics": topics,"comments":comments}
    return render(request, "home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("comment")
        )
        room.participants.add(request.user)
        return redirect("room", pk=room.id)
    context = {"room": room, "room_messages": room_messages,"participants":participants}
    return render(request, "room.html", context)


@login_required(login_url="login")
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "room_form.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"room": room}
    return render(request, "delete.html", context)


def user_login(request):
    page = "login_page"
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            print(username, password)

        except:
            print("user not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("<h1>User Not Registered</h1>")
    context = {"page": page}
    return render(request, "login_register.html", context)


def user_logout(request):
    logout(request)

    return redirect("home")


def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")
    context = {"form": form}
    return render(request, "login_register.html", context)


@login_required(login_url="login")
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        return redirect("home")
    context = {"message": message}
    return render(request, "delete.html", context)
