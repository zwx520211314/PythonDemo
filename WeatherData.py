
import requests as req
import requests as req
import json
import json
import json
import json
class WeatherDate:
    temperature = ''
    humid = ''
    key = 'bf1b626f3ed6c480088d28d9a053e358'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    icon = ''
    def __init__(self, city):
        self.city = city
        apiURL = '{url}?q={city}&APPID={key}'.format(
        url = self.url,
        city = self.city,
        key = self.key
        )
        print(apiURL)
        r = req.get(apiURL)
        obj = json.loads(r.text)
        self.icon = obj['weather'][0]['icon']
        self.humid = obj['main']['humidity']
    def getTemperature(self):
         print(type(self.temperature))
         return str(self.temperature)
    def getHumid(self):
        return self.humid 
if __name__ == "__main__":
    current_weather = WeatherDate('Shanghai, cn')
    print(current_weather.getHumid())
