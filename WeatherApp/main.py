import tkinter as tk

import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def get_data():
    place = input_place.get()
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}"
        )
        result = response.json()
        print(result['cod'])

        if(result['cod'] != 200):
            # weather_Result.config(text = f"{place} not found")
            weather_Result.config(text = result['message'])
            return

        latitude = result['coord']['lat']
        longitude = result['coord']['lon']
        description = result['weather'][0]['description']
        temp = result['main']['temp']
        max_temp = result['main']['temp_max']
        min_temp = result['main']['temp_min']
        weather_Result.config(text = f"{place} \n Latitude : {latitude}\n Longitute : {longitude} \n{description} \n Temperature : {temp}K\n Max Temperature : {max_temp}K\n Min Temperature : {min_temp}K")

    except requests.exceptions.RequestException as e:
        print("Error IS", e)

    finally:
        input_place.delete(0, tk.END)


root = tk.Tk()

root.title("Weather Application")


label = tk.Label(root, text="Enter Place")
label.pack()

input_place = tk.Entry(root, font=("Arial", 12, "bold"))
input_place.pack()

get_Button = tk.Button(root, text="Get Weather", command=get_data)
get_Button.pack()

weather_Result = tk.Label(root, text=" ")
weather_Result.pack()
root.mainloop()
