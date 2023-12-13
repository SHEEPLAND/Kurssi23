import requests

def kelvin_to_celcius(kelvin):
    return kelvin-273

def get_city_coordinates(api_key, city):
    base_url ='http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': city,
        'limit': 1,
        'appid': api_key
    }

    res = requests.get(base_url, params=params)

    if res.status_code == 200:
        data = res.json()
        coords = data[0]['lat'], data[0]['lon']
        print(coords)
        return coords
    else:
        print('Virhe koordinaattien hakemisessa')

def get_weather(api_key, lat, lon, city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }

    res = requests.get(base_url, params=params)

    if res.status_code == 200:
        data = res.json()
        description = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celcius = kelvin_to_celcius(temp_kelvin)

        print(f'------[{city_name}]------')
        print(f'Temperature: {temp_celcius:.0f} degrees celcius')
        print(f'Description: {description}')
    else:
        print('Virhe säätietojen hakemisessa')

if __name__ == '__main__':
    api_key = 'f806590ff13e2499734e34a745c8ee63'
    city_name =  input('Anna paikkakunnan nimi: ').lower()
    lat, lon = coords = get_city_coordinates(api_key, city_name)
    get_weather(api_key, lat, lon, city_name)
