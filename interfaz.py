import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame, Label
from PIL import ImageTk, Image
import record_audio
import show_similarities
from build_database import build_db
import time

def update_progress(value):
    prog_bar["value"] = value
    ventana.update()


def your_time_consuming_function():
    print("Starting function")
    update_progress(0)
    time.sleep(2)
    print("I reached my first checkpoint")
    update_progress(25)
    time.sleep(2)
    print("Another checkpoint, yay")
    update_progress(50)
    time.sleep(2)
    print("Only 1 more to go")
    update_progress(75)
    time.sleep(2)
    print("Yay im finished")
    update_progress(100)

def mostrar_cancion():
    record_audio.record()
    etiqueta_temp_kelvin.config(text=f"La canción se ha grabado")
    # Most probable song
    song = show_similarities.print_top_five('recording.wav', song_name_index, database)
    etiqueta_temp_fahrenheit.config(
        text=song)

    print(song+'.jpg')
    img = Image.open(f"Imagenes canciones/Imagenes canciones/{song}.jpg").resize((700, 500), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img)
    panel.configure(image=new_image)
    panel.image = new_image
    update_progress(0)
# def mostrar_barra():

song_name_index, database = build_db()

ventana = tk.Tk()


ventana.title("CHAZAM")
# Define the geometry of the window
ventana.geometry("700x500")
# ventana.config(width=400, height=300)

frame = Frame(ventana, width=50, height=50)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5, )


# Create an object of tkinter ImageTk
im = Image.open("Imagenes Canciones/Imagenes Canciones/pandabb.jpg")
# image1 = im.resize((400, 400))
img = ImageTk.PhotoImage(im)

# label = Label(frame, image = img)
panel = tk.Label(ventana, image=img) # PARA EL BACKGROUND 
panel.pack()

etiqueta_temp_celsius = ttk.Label(text="BIENVENIDO A CHAZAM",font=("Ahroni",28),foreground="white",background="black")
etiqueta_temp_celsius.place(x=30, y=20)

# caja_temp_celsius = ttk.Entry()
# caja_temp_celsius.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(ventana,text="Grabar", command=lambda:[your_time_consuming_function(),mostrar_cancion()], width=10)
boton_convertir.place(x=30,y=100)

# Create a progressbar to show the progress of recording
prog_bar = ttk.Progressbar(ventana,
    orient='horizontal',
    mode='determinate')
prog_bar.place(x=110, y=100)

etiqueta_temp_kelvin = ttk.Label(text="LEYENDO CANCIÓN",font=("Ahroni",12),foreground="white", background="black")
etiqueta_temp_kelvin.place(x=30, y=160,)
etiqueta_temp_fahrenheit = ttk.Label(text="Tu canción es...",font=("Ahroni",20))
etiqueta_temp_fahrenheit.place(x=30, y=200)

ventana.mainloop()