import tkinter as tk

def get_data():
    place = input_place.get()
    print(place)
    
root = tk.Tk()

root.title("Weather Application")


label = tk.Label(root, text="Enter Place")
label.pack()

input_place = tk.Entry(root, font=("Arial", 15, "bold"))
input_place.pack()

get_Button = tk.Button(root,text = "Get Weather", command = get_data)
get_Button.pack()
root.mainloop()



