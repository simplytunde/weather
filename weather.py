import requests

WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "73511d60d65c4b15be62c52a91039247"

def getCityWeather(**kwargs):
    """Get weather for a city based on name or id.
    This function accepts positional arguments like city_id=123 or city_name = "Los Angeles"

    Keyword Arguments:
    city_id: id of the city
    city_name: name of the city if id is not available.
    """
    payload = {'appid':WEATHER_API_KEY}
    if 'city_id' in kwargs:
        payload['city_id']=kwargs.get('city_id')
    elif 'city_name' in kwargs:
        payload['city_query']=kwargs.get('city_name')
    else:
        raise Exception("Invalid Arguments: Please enter the city_id or city_name") 
    r = requests.get(WEATHER_API_URL, params=payload)
    print(r.url)
    return r.json()

if __name__ == "__main__":
    print(getCityWeather(city_name="Los Angeles"))