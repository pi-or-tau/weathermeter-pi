import requestor as rq
import time

def k2f(kel):
    far = round(((kel - 273.15) * (9/5) + 32),2)
    return far

class vari_init:
    def __init__(self):
        self.t = rq.req()
        self.temp_K = self.t['main']['temp']
        self.temp_F = k2f(self.temp_K)
        self.weather_id = self.t['weather'][0]['id']
        self.weather_main = self.t['weather'][0]['main']
        self.weather_description = self.t['weather'][0]['description']
        self.icon = self.t['weather'][0]['icon']
        self.pressure = self.t['main']['pressure']
        self.humidity = self.t['main']['humidity']
        self.temp_min_F = k2f(self.t['main']['temp_min'])
        self.temp_max_F = k2f(self.t['main']['temp_max'])
        self.windspeed = self.t['wind']['speed']
        self.cloud_percent = self.t['clouds']['all']
        self.time_taken = time.strftime("%I:%M %p",time.localtime(self.t['dt']))
        self.sunrise = time.strftime("%I:%M %p",time.localtime(self.t['sys']['sunrise']))
        self.sunset = time.strftime("%I:%M %p",time.localtime(self.t['sys']['sunset']))
'''
current = vari_init()

print('Temperature: ' + str(current.temp_F) + 'F')
print('Weather: ' + current.weather_description)
print('Sunrise: ' + current.sunrise)
print('Sunset: ' + current.sunset)
print('At: ' + current.time_taken)
'''
