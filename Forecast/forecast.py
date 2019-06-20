'''
Created on 27 мая 2019 г.

@author: m.elagina
'''
import pyowm
owm = pyowm.OWM('673e81afc329079353e763f282830af6', language = 'ru')  # You MUST provide a valid API key
place = input("input  location: ")
observation = owm.weather_at_place(place )
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]
print(w.get_detailed_status())
print(w.get_humidity())
print(temp)

if temp < 10:
    print("холодно")
elif temp < 20:
    print("прохладно")
else:     
    print("тепло")
        