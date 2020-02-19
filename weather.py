#! /usr/local/bin/python3
import requests

WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "73511d60d65c4b15be62c52a91039247" #obtain your API key from your account, this is from the website

def getCityWeather(**kwargs):
    """Get weather for a city based on name or id.
    This function accepts positional arguments like city_id=123 or city_name = "Los Angeles"

    Keyword Arguments:
    city_id: id of the city
    city_name: name of the city if id is not available.
    """
    payload = {'appid':WEATHER_API_KEY}
    if 'city_id' in kwargs:
        payload['id']=kwargs.get('city_id')
    elif 'city_name' in kwargs:
        payload['q']=kwargs.get('city_name')
    elif 'zip' in kwargs:
        payload['zip']=kwargs.get('zip')
    elif "lat" in kwargs and "lon" in kwargs:
        payload['lat']=kwargs.get('lat')
        payload['lon']=kwargs.get('lon')
    else:
        raise Exception("Invalid Arguments: Please enter the city_id or city_name") 
    r = requests.get(WEATHER_API_URL, params=payload)
    if r.status_code == requests.codes.ok:
        weather_description = ""
        for desc in r.json()["weather"]:
            weather_description += desc["description"] + ","
        return weather_description[:-1] #remove last ,
    else:
        raise Exception(r.json()["message"])
    return None


if __name__ == "__main__":
    city_name = "Los Angeles"
    print(f"Weather In {city_name}: ",getCityWeather(city_name=city_name))