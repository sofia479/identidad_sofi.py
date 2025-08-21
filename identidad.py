from tkinter import *
from tkinter import messagebox

# -----------------------------
# ventana principal de la app
# -----------------------------

ventana_principal = Tk()
ventana_principal.title("Aplicacion de Fofi")
ventana_principal.geometry("650x650")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

# --------------------------------
# frame entrada datos
# --------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=630, height=180)
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text="Sofia Galvis")
titulo.config(bg="white", fg="blue", font=("Helvetica", 25))
titulo.place(x=230, y=30)

titulo2 = Label(frame_entrada, text= "YO PUEDO SOLA,SIN AYUDA DE NADIE.")
titulo2.config(bg="white", fg="black", font=("Verdana", 14))
titulo2.place(x=198, y=80)

logo = PhotoImage(file="img/Fofi.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=10)



# --------------------------------
# frame botoncitos 1
# --------------------------------
frame_botones1 = Frame(ventana_principal)
frame_botones1.config(bg="blue", width=630, height=180)
frame_botones1.place(x=10, y=200)

# --------------------------------
# frame botoncitos 2
# --------------------------------
frame_botones2 = Frame(ventana_principal)
frame_botones2.config(bg="orange", width=630, height=245)
frame_botones2.place(x=10, y=390)

# --------------------------------
# funciones para abrir ventanas
# --------------------------------

def abrir_ventana1():
    v1 = Toplevel()
    v1.title("Ventana 1")
    v1.geometry("400x300")
    v1.config(bg="lightgray")

def abrir_ventana2():
    v2 = Toplevel()
    v2.title("Ventana 2")
    v2.geometry("400x300")
    v2.config(bg="lightgray")

def abrir_ventana3():
    v3 = Toplevel()
    v3.title("Ventana 3")
    v3.geometry("400x300")
    v3.config(bg="lightgray")

def abrir_ventana4():
    v4 = Toplevel()
    v4.title("Ventana 4")
    v4.geometry("400x300")
    v4.config(bg="lightgray")

def abrir_ventana5():
    v5 = Toplevel()
    v5.title("Ventana 5")
    v5.geometry("400x300")
    v5.config(bg="lightgray")

def abrir_ventana6():
    v6 = Toplevel()
    v6.title("Ventana 6")
    v6.geometry("400x300")
    v6.config(bg="lightgray")

def abrir_ventana7():
    v7 = Toplevel()
    v7.title("Ventana 7")
    v7.geometry("400x300")
    v7.config(bg="lightgray")

def abrir_ventana8():
    v8 = Toplevel()
    v8.title("Ventana 8")
    v8.geometry("400x300")
    v8.config(bg="lightgray")

def abrir_ventana9():
    v9 = Toplevel()
    v9.title("Ventana 9")
    v9.geometry("400x300")
    v9.config(bg="lightgray")

def abrir_ventana10():
    v10 = Toplevel()
    v10.title("Ventana 10")
    v10.geometry("400x300")
    v10.config(bg="lightgray")

# --------------------------------
# Botones en frame 1
# --------------------------------

btn1 = Button(frame_botones1, text="Botón 1", command=abrir_ventana1)
btn1.place(x=20, y=70, width=100, height=30)

btn2 = Button(frame_botones1, text="Botón 2", command=abrir_ventana2)
btn2.place(x=140, y=70, width=100, height=30)

btn3 = Button(frame_botones1, text="Botón 3", command=abrir_ventana3)
btn3.place(x=260, y=70, width=100, height=30)

btn4 = Button(frame_botones1, text="Botón 4", command=abrir_ventana4)
btn4.place(x=380, y=70, width=100, height=30)

btn5 = Button(frame_botones1, text="Botón 5", command=abrir_ventana5)
btn5.place(x=500, y=70, width=100, height=30)

# --------------------------------
# Botones en frame 2
# --------------------------------

btn6 = Button(frame_botones2, text="Botón 6", command=abrir_ventana6)
btn6.place(x=20, y=100, width=100, height=30)

btn7 = Button(frame_botones2, text="Botón 7", command=abrir_ventana7)
btn7.place(x=140, y=100, width=100, height=30)

btn8 = Button(frame_botones2, text="Botón 8", command=abrir_ventana8)
btn8.place(x=260, y=100, width=100, height=30)

btn9 = Button(frame_botones2, text="Botón 9", command=abrir_ventana9)
btn9.place(x=380, y=100, width=100, height=30)

btn10 = Button(frame_botones2, text="Botón 10", command=abrir_ventana10)
btn10.place(x=500, y=100, width=100, height=30)

# -----------------------------
# run
# -----------------------------
ventana_principal.mainloop()