from django.shortcuts import render
from .models import Room
# Create your views here.
def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }
    return render(request, 'home.html', context)

def room_page(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {
        'room': room,
    }
    return render(request, 'room_page.html', context)