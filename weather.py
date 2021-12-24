import requests
import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
l1=tk.Label(textvariable='')
l2=tk.Label(textvariable='')
l3=tk.Label(textvariable='')
l1.pack
l3.pack
l2.pack
window.title('my window')
window.geometry('500x300')
url = 'https://api.openweathermap.org/data/2.5/weather?q='
v1 = tk.StringVar()
entry01 = tk.Entry(textvariable=v1)
entry01.pack()
def search():
    global l1
    global l2
    global l3
    l2.destroy()
    l3.destroy()
    l1.destroy()
    city=v1.get()
    response = requests.get(url + city + '&units=metric&APPID=867d2a2cdeb331e8be895ee2d4fb4e7d')
    d = response.json()
    if(d['cod'] == 200):
        l2.destroy()
        l3.destroy()
        l1.destroy()
        cc=("City：", d["name"], d["sys"]["country"])
        t=("temp：", "Lowest-Temp", d["main"]["temp_min"], "°C", "Highest-Temp", d["main"]["temp_max"], "°C")
        w=("Weather：", d["weather"][0]["main"])
        l1 = tk.Label(text=cc)
        l1.pack()
        l2 = tk.Label(text=t)
        l2.pack()
        l3 = tk.Label(text=w)
        l3.pack()
    else:
        l2.destroy()
        l3.destroy()
        l1.destroy()
        tk.messagebox.showerror(message=d["message"])
btn01 = tk.Button(text='search', command=search)
btn01.pack()
window.mainloop()