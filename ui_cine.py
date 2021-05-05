from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

sala = StringVar()
butakas = StringVar()
boletos = StringVar()
precio = StringVar()

def crear_sala():
    sala = entry_sala.get()
    butakas = entry_butakas.get()
    boletos = entry_boletos.get()
    precio = entry_precio.get()

    cine_db = cine_database.Mydatabase()
    cine_db.insert_db(sala, butakas, boletos, precio)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_food.place(x=25, y=30)
label_sala = Label(frame_food, 
              text="SALA:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_sala.place(x=20, y=60)
entry_sala = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_sala.place(x=20, y=100)

label_butakas = Label(frame_food, 
              text="BUTAKAS:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_butakas.place(x=20, y=130)
entry_butakas = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"), show="*")
entry_butakas.place(x=20, y=170)

label_boletos = Label(frame_food, 
              text="BOLETOS:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_boletos.place(x=20, y=200)
entry_boletos = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_boletos.place(x=20, y=240)

label_boletos = Label(frame_food, 
              text="PRECIO:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_boletos.place(x=20, y=280)
entry_boletos = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_boletos.place(x=20, y=310)

button_register = Button(frame_food, text="ASIGNAR", 
                        font=("Calibri", "14", "bold", command="crear_sala"))
button_register.place(x=20, y=350)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="¡Bienvenido(a)!", 
              font=("Calibri", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="CINE ", 
              font=("Calibri", "18"),
              justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()
