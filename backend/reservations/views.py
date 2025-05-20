from rest_framework import generics
from django.db.models import Sum
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingAvailability(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', None)
        time = self.request.query_params.get('time', None)
        party_size = self.request.query_params.get('party_size', None)
        if date and time and party_size:
            total_booked = Booking.objects.filter(date=date, time=time).aggregate(total=Sum('party_size'))['total'] or 0
            max_capacity = 20
            remaining = max_capacity - total_booked
            return Booking.objects.filter(date=date, time=time) if remaining < int(party_size) else []
        return Booking.objects.none()