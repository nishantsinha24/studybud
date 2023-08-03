from django.shortcuts import render
from .models import Room
# Create your views here.
#rooms = [
#    {'id' : 1, 'name' : 'lets learn Python !'},
#    {'id' : 2, 'name': 'let us code in Java!'},
#    {'id' : 3, 'name': 'we can do PHP as well'},
#]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html' , context)
