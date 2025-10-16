from django.contrib import admin
# Register your models here.
from .models import Room
admin.site.register(Room)
from .models import Booking
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'guests', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('room__title', 'user__username', 'user__email', 'phone')

admin.site.register(Booking, BookingAdmin)