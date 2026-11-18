import json
from django.shortcuts import render, get_object_or_404
from .models import Place

def home(request):
    popular_places = Place.objects.all()[:4]
    featured_place = Place.objects.filter(name__icontains="Koneswaram").first() 
    if not featured_place:
        featured_place = Place.objects.first() 
    return render(request, 'places/home.html', {'popular_places': popular_places, 'featured_place': featured_place})

def place_list(request):
    # 1. Start with all places
    places = Place.objects.all()
    
    # 2. Get the search query from the URL
    search_query = request.GET.get('search', '').strip()
    
    # 3. Get the category from the URL
    category = request.GET.get('category', '').strip()
    
    # 4. Apply the filters
    if category:
        places = places.filter(category=category)
        
    if search_query:
        # Filter by name (case-insensitive)
        places = places.filter(name__icontains=search_query) 

    # 5. Send data to the HTML
    context = {
        'places': places,
        'current_search': search_query,
        'current_category': category
    }
    
    return render(request, 'places/list.html', context)

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'places/detail.html', {'place': place})

def map_view(request):
    places = Place.objects.all()
    # We package the data exactly how the map needs it
    places_data = [{
        'id': p.id, 
        'name': p.name, 
        'lat': p.latitude, 
        'lng': p.longitude, 
        'category': p.category, 
        'distance': str(p.distance)
    } for p in places]
    
    # We pass it directly as a Python list, Django's json_script will handle the conversion safely
    return render(request, 'places/map.html', {'places_data': places_data})

def itinerary(request):
    return render(request, 'places/itinerary.html')
