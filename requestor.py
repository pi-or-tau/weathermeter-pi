import requests
import json

def req():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=32601,us&appid=b63f6e65501af7f727c6d5fe1af4b101')
    t = json.loads(r.text)
    return t
