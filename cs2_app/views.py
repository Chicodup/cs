from django.contrib import messages
from django.shortcuts import render, redirect
from cs2_app.models import Room, Booking
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def room_page(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')
        phone = request.POST.get('phone')

        if check_in and check_out and guests and phone:
            is_booked = Booking.objects.filter(
                room=room,
                check_in__lte=check_in,
                check_out__gt=check_in,
            )
            
            if is_booked.exists():
                messages.error(request, 'This room is already booked for the selected dates.')
            else:
                Booking.objects.create(
                    user=request.user,
                    room=room,
                    check_in=check_in,
                    check_out=check_out,
                    guests=guests,
                    phone=phone,
                )
                messages.success(request, 'Room booked successfully!')
                return redirect('home')
    context = {
        'room': room,
    }
    return render(request, 'room_page.html', context)