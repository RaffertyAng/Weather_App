from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        api_key = 'e47a6b393fa3f32e5fa313044a544c1d'
        new_city = request.form.get('newCity')
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={new_city}&units=metric&APPID={api_key}"
        )

        if weather_data.json()['cod'] == '404':
            weather = "City not found"
            temp = None
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

        return render_template("weather.html", city=new_city, weather=weather, temp=temp)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)