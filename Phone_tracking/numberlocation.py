import phonenumbers
from mynumber import number
from phonenumbers import geocoder,carrier
from opencage.geocoder import OpenCageGeocode
import folium

KEY = "ef8e822acd354c7b97d1b82a5b1d76f4"
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber,'en')
print(yourLocation)

#service provider
serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider,'en'))

geocoder = OpenCageGeocode(KEY)
query = str(yourLocation)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

#save
myMap.save('myLocation.html')