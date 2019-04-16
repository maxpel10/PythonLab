from MMat import *
from CMat import *
from tkinter import *
from tkinter import messagebox

class ABMCMateria:
    def __init__(self, bd, abierto):
        if abierto:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 432
            h = 55
            ws = pantalla.winfo_screenwidth()
            hs = pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            width = 20
            heigth = 2
            colorboton = "#20B2AA"
            colorletra = "#B22222"
            fuente = "Helvetica 12 bold italic"
            borde = 5
            pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            pantalla.title('ABMC materia')
            bmodificar = Button(pantalla,  height=heigth, width=width, relief="raised", borderwidth=borde,
                                background=colorboton,
                                fg=colorletra, font=fuente, text="Modificar materia", command=lambda: MMat(bd))
            bmodificar.grid(row=0, column=0)
            bconsulta = Button(pantalla,  height=heigth, width=width, relief="raised", borderwidth=borde,
                               background=colorboton,
                               fg=colorletra, font=fuente, text="Consultar materia", command=lambda: CMat(bd))
            bconsulta.grid(row=0, column=1)
            pantalla.mainloop()
        else:
            messagebox.showwarning("Advertencia", "No ha iniciado la sesion de trabajo.")
