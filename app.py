import requests

api_key = 'e47a6b393fa3f32e5fa313044a544c1d'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"Current weather in {user_input}:")
    print(f"{weather}")
    print(f"{temp} °C")
