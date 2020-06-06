from django.shortcuts import render
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializers,PassengerSerializers,ReservationSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def find_flights(request):
    flight = Flight.objects.filter(departure_city=request.data['departure_city'],
                                   arrival_city=request.data['arrival_city'],
                                   date_of_departure=request.data['date_of_departure']
                                   )
    serialize = FlightSerializers(flight, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightID'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    Reservation.save(reservation)

    return Response(status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers

