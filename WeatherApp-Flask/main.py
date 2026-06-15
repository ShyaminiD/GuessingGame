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

        place = request.args.get("place", "").strip()
        display_place = place
        if not place:
            defaultlocation_response = requests.get("http://ip-api.com/json/").json()
            print(defaultlocation_response["city"])
            place = defaultlocation_response["city"]

        print("PLACE", place)
        if place:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
            response = requests.get(url)
            weatherData = response.json()
            print(weatherData)
            print("HELLO World")
        if weatherData:
            display_place = " "
    return render_template("index.html", place=display_place, weatherData=weatherData)


@app.route("/about")
def AboutPage():
    return "This is the About Page"


if __name__ == "__main__":
    app.run(debug=True)
