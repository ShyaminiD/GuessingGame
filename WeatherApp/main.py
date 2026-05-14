import tkinter as tk

import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")



def get_Weather(place):
    try :
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}")
        result = response.json()
        print(result)
        latitude = result['coord']['lat']
        longitude = result['coord']['lon']
        description = result['weather'][0]['description']
        temp = result['main']['temp']
        max_temp = result['main']['temp_max']
        min_temp = result['main']['temp_min']
        weather_Result.config(text = f"{place} \n Latitude : {latitude}\n Longitute : {longitude} \n{description} \n Temperature : {temp}\n Max Temperature : {max_temp} \n Min Temperature : {min_temp}")

    except  requests.exceptions.RequestException as e:
        print(e)


def get_data():
    place = input_place.get()
    get_Weather(place)
   
    
    
root = tk.Tk()

root.title("Weather Application")


label = tk.Label(root, text="Enter Place")
label.pack()

input_place = tk.Entry(root, font=("Arial", 12, "bold") )
input_place.pack()

get_Button = tk.Button(root,text = "Get Weather", command = get_data)
get_Button.pack()

weather_Result = tk.Label(root, text= "Result is ")
weather_Result.pack()
root.mainloop()



