from django.shortcuts import render
from django.views.generic import View
import folium
import geocoder

from .models import Search

# Create your views here.

def Home(request, template_name= "map/index.html"):
    context = {}
        
    # Search address
    address = Search.objects.all().last()
    # location
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    
    
    # map object
    m = folium.Map(location=[19,-12,], zoom_start=2)
    #folium.Marker([4.594, -0.219],tooltip="click for more", popup='DRC').add_to(m)
    
    
    folium.Marker([lat, lng],tooltip="click for more", popup=country).add_to(m)
    #  get html representation of map object
    m = m._repr_html_()
        
    context['m'] = m
    return render(request, template_name, context)

    

# Create your views here.

# class Home(View):
    
#     template_name= "map/index.html"
    
#     def get_context_data(self, request, **kwargs):
#         context = {}
        
#         # Search address
#         address = request.POST.get('seach')
#         # location
#         location = geocoder.osm(str(address))
#         lat = location.lat
#         lng = location.lng
#         country = location.country
        
       
#         # map object
#         m = folium.Map(location=[19,-12,], zoom_start=2)
#         folium.Marker([4.594, -0.219],tooltip="click for more", popup='DRC').add_to(m)
        
       
#         folium.Marker([lat, lng],tooltip="click for more", popup=country).add_to(m)
#         #  get html representation of map object
#         m = m._repr_html_()
            
#         context['m'] = m
#         return context
    
