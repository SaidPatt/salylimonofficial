from django.contrib import admin
from django.urls import path, include
from reservations.views import BookingListCreate, BookingAvailability  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bookings/', include('reservations.urls')),
]