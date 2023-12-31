from django.shortcuts import render, redirect
from .models import Room
from .form import RoomForm
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
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html' , context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room )
        if form.is_valid(): 
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request, 'base/room_form.html' , context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html' , {'obj' : room})