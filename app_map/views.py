from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
import folium
import geocoder

# Create your views here.



# Create your views here.

class Home(TemplateView):
    
    template_name= "map/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # location
        location = geocoder.osm('UK')
        lat = location.lat
        lng = location.lng
        country = location.country
        # map object
        m = folium.Map(location=[19,-12,], zoom_start=2)
        folium.Marker([4.594, -0.219],tooltip="click for more", popup='DRC').add_to(m)
        
       
        folium.Marker([lat, lng],tooltip="click for more", popup=country).add_to(m)
        #  get html representation of map object
        m = m._repr_html_()
            
        context['m'] = m
        return context
    
