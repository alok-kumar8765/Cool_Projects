from numpy import int32
import requests
import folium
import phonenumbers
from mynumber import number
from phonenumbers import geocoder

res = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(res,'en')

# res = requests.get('https://ipinfo.io')
# data = res.json
lat = yourLocation[0]
log = yourLocation[1]

fg = folium.FeatureGroup('my map')
# fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sg').read())))
# fg.add_child(folium.Marker(location=[lat,log],popup="this is location"))
# map = folium.Map(location=[lat,log],zoom_start=9)
myMap=fg.add_child(folium.Map(location=[lat,log],zoom_start=9))
fg.add_child(folium.Marker([lat,log],popup=yourLocation).add_to(myMap))
# map.add_child(fg)
map.save("map.html")