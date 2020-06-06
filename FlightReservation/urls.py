from django.contrib import admin
from django.urls import path,include
from FlightApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flightapi/', include(router.urls)),
    path('flightapi/findflights/', views.find_flights),
    path('flightapi/saveReservation/', views.save_reservation)
]
