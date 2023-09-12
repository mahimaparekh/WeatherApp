import requests


def city_name():
    while True:
        city = input('Enter city name: ')
        api_key = '################################'
        url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"
        response = requests.get(url).json()
        if 'message' in response and response['message'] == 'city not found':
            print('City not found. Try again')
            continue
        else:
            try:
                print('\nChoose a temperature display option from below')
                print('1. Celsius')
                print('2. Fahrenheit')
                print('3. Kelvin')
                t = input('Choice: ')
                n = validation1(t, 2)

                temp = round(temp_converter1(n, response['main']['temp']), 2)
                feels_like = round(temp_converter1(n, response['main']['feels_like']), 2)
                temp_min = round(temp_converter1(n, response['main']['temp_min']), 2)
                temp_max = round(temp_converter1(n, response['main']['temp_max']), 2)
                pressure = round(response['main']['pressure'], 2)
                humidity = round(response['main']['humidity'], 2)
                description = response['weather'][0]['description']
                des_statements(n, city, temp, feels_like, temp_min, temp_max, pressure, humidity, description)

            except ValueError:
                print('Invalid Choice. Try again')
        break


def geo_location():
    base_url = f'https://api.openweathermap.org/data/2.5/weather'
    while True:
        latitude = input('Enter latitude: ')
        longitude = input('Enter longitude: ')
        validation2(latitude, longitude)

        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': '################################',
            'units': 'metric'
        }
        response = requests.get(base_url, params=params).json()

        if 'message' in response and (response['message'] == 'wrong latitude' or response['message'] == 'wrong longitude'):
            print('\nInvalid longitude and latitude values. Try again')
            continue
        else:
            try:
                print('\nChoose a temperature display option from below')
                print('1. Celsius')
                print('2. Fahrenheit')
                print('3. Kelvin')
                t = input('Choice: ')
                n = validation1(t, 2)

                city = response['name']

                temp = round(temp_converter2(n, response['main']['temp']), 2)
                feels_like = round(temp_converter2(n, response['main']['feels_like']), 2)
                temp_min = round(temp_converter2(n, response['main']['temp_min']), 2)
                temp_max = round(temp_converter2(n, response['main']['temp_max']), 2)
                pressure = round(response['main']['pressure'], 2)
                humidity = round(response['main']['humidity'], 2)
                description = response['weather'][0]['description']

                des_statements(n, city, temp, feels_like, temp_min, temp_max, pressure, humidity, description)

            except ValueError:
                print('Invalid Choice. Try again')
        break


def temp_converter1(num, value):
    if num == 1:
        celsius = value - 273.15
        return celsius

    elif num == 2:
        fahrenheit = (value - 273.15) * (9 / 5) + 32
        return fahrenheit
    else:
        return value


def temp_converter2(num, value):
    if num == 1:
        return value

    elif num == 2:
        fahrenheit = (value * (9 / 5)) + 32
        return fahrenheit
    else:
        kelvin = value + 273.15
        return kelvin


def des_statements(n, city, temp, feels_like, temp_min, temp_max, pressure, humidity, description):
    if n == 1:
        print('\n'
              f'The current temperature in {city.capitalize()} is {temp} °C. However, it feels like {feels_like} °C.'
              f'\nThe minimum temperature recorded is {temp_min} °C while the max temperature is {temp_max} °C. '
              f'\nThe atmospheric pressure stands at {pressure} hPa with humidity level at {humidity} %.'
              f'\nThe city of {city.capitalize()} will see {description} today.')
    elif n == 2:
        print('\n'
              f'The current temperature in {city.capitalize()} is {temp} °F. However, it feels like {feels_like} °F.'
              f'\nThe minimum temperature recorded is {temp_min} °F while the max temperature is {temp_max} °F.'
              f'\nThe atmospheric pressure stands at {pressure} hPa with humidity level at {humidity} %.'
              f'\nThe city of {city.capitalize()} will see {description} today.')
    else:
        print('\n'
              f'The current temperature in {city.capitalize()} is {temp} K. However, it feels like {feels_like} K. '
              f'\nThe minimum temperature recorded is {temp_min} K while the max temperature is {temp_max} K.'
              f'\nThe atmospheric pressure stands at {pressure} hPa with humidity level at {humidity} %.'
              f'\nThe city of {city.capitalize()} will see {description} today.')


def validation1(c, n):
    ul = 0
    if n == 1:
        ul = 2
    elif n == 2:
        ul = 3
    while True:
        try:
            if c.lower() == 'q':
                return c
            c1 = int(c)
            if 1 <= c1 <= ul:
                return c1
            else:
                print('\nInvalid Input. Try again')
                c = input('Enter choice: ')
        except ValueError:
            print('\nInvalid Input. Try again')
            c = input('Enter choice: ')


def validation2(lat, lon):
    while True:
        try:
            lt = float(lat)
            ln = float(lon)
            return lt, ln
        except ValueError:
            print('\nInvalid Input. Try again')
            lat = input('Enter latitude: ')
            lon = input('Enter longitude: ')


if __name__ == '__main__':
    print('\n\tWelcome to the Weather App')
    print('-----------------------------------')

    while True:
        print('\nChoose from the options below')
        print('1. Enter city name: ')
        print('2. Use geolocation: ')
        print('Press q to quit')
        try:
            choice = input('Enter choice: ').strip()
            if choice == 'q':
                print('\nYou have exited the program.'
                      'Thank you for using the Weather App')
                break
            else:
                val = validation1(choice, 1)

                match val:
                    case 'q':
                        print('\nYou have exited the program.'
                              'Thank you for using the Weather App')
                        break
                    case 1:
                        city_name()
                    case 2:
                        geo_location()
        except ValueError:
            print('Invalid Input. Try again')
