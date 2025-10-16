from django.db import models
from django.contrib.auth.models import User



class Room(models.Model):
    type_choise = [
        ('standart', 'Standart'),
        ('lux', 'Lux'),
        ('suite', 'Suite'),
    ]
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    type_room = models.CharField(choices=type_choise, max_length=50, default='standart')
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guests = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.room} in {self.check_in} by {self.check_out}'