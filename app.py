from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    weather = None
    temp = None
    city = None

    if request.method == 'POST':
        api_key = 'e47a6b393fa3f32e5fa313044a544c1d'
        new_city = request.form.get('newCity')
        if new_city:
            city = new_city
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
            )
            weather_json = weather_data.json()

            if weather_json['cod'] == '404':
                error = "City not found. Please enter a valid city name."
            else:
                weather = weather_json['weather'][0]['main']
                temp = round(weather_json['main']['temp'])

    return render_template("weather.html", city=city, weather=weather, temp=temp, error=error)

if __name__ == "__main__":
    app.run(debug=True)
