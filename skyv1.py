import json
import requests
import time
import datetime
from geopy.geocoders import Nominatim

city = input("Enter City Name: ")
postcode = input("Enter Your Postcode: ")
api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=48e90e11d28d64940a23316594ce606e"
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp'] - 273.15)
min_temp = int(json_data['main']['temp_min'] - 273.15)
max_temp = int(json_data['main']['temp_max'] - 273.15)
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
windspeed = json_data['wind']['speed']
sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 3600))
sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 3600))

final_info = condition + "\n" + str(temp) + "°c"
final_data = '\n' + "Max Temp: " + str(max_temp) + '\n' + "Min Temp: " + str(min_temp) + '\n' + "Pressure: " + str(pressure) + '\n' + "Humidity: " + str(humidity) + '\n' + "Windspeed: " + str(windspeed) + "mph " + '\n' + "Sunrise: " + sunrise + '\n' + "Sunset: " + sunset 

geolocator = Nominatim(user_agent="sky")
location = geolocator.geocode(postcode)

def cityInfo():
    print(city)

def weatherInfo():
    print(final_info + final_data)

def locationInfo():
    print(location)
    print(location.raw)

weatherInfo()
locationInfo()
cityInfo()
