from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("API_KEY")

@app.context_processor
def getWeather():
    weatherData = None
    errorfromApi = None
    fiveDaysData = None
 

    try:
        if request.method == "GET":
            print("GET method")

            place = request.args.get("place", "").strip()
            display_place = place
            if not place:
                defaultlocation_response = requests.get(
                    "http://ip-api.com/json/"
                ).json()
                print(defaultlocation_response["city"])
                place = defaultlocation_response["city"]

                print("PLACE", place)
            if place:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
                response = requests.get(url)
                weatherData = response.json()
                # print("xxxxxxxxxxxxxx",weatherData)
                urlfivedays = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units=metric"
                responseFiveDays = requests.get(urlfivedays)
                fiveDaysData = responseFiveDays.json()
                print("FIVE DAYS DATA : ", fiveDaysData)
              
                fiveDaysForecast = fiveDaysData["list"]
                for i in fiveDaysForecast:
                    print("i",i)
                
              
            if weatherData:
                display_place = " "
    except Exception as e:
        print("Place not found", e)
    return {
    "weatherData": weatherData,
    "fiveDaysData":fiveDaysData,
    "fiveDaysForecast":fiveDaysForecast
}

@app.route("/", methods=["GET", "POST"])
def HomePage():
   return render_template(
            "home.html",
   )

@app.route("/home")
def Home():
   return render_template(
            "home.html",
   )
   
@app.route("/about")
def About():
   return render_template(
            "about.html",
   )
@app.route("/5days", methods=["GET", "POST"])
def FiveDays():
   return render_template(
            "fivedays.html",
   )
   
if __name__ == "__main__":
    app.run(debug=True)
