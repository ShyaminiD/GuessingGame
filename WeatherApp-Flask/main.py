from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")


@app.route("/", methods=["GET", "POST"])
def HomePage():
    weatherData = None
    if request.method == "GET":
        print("GET method")
        place = request.args.get("place","").strip()
        print("PLACE", place)
        if place:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
            response = requests.get(url)
            weatherData = response.json()
            print(weatherData)
            print("HELLO World")

    return render_template("index.html", place=place, weatherData=weatherData)


if __name__ == "__main__":
    app.run(debug=True)
