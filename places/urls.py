from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.place_list, name='place_list'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
    path('map/', views.map_view, name='map_view'),
    path('itinerary/', views.itinerary, name='itinerary'),
]