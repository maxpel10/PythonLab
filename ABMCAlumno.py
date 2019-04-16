from AAlumno import *
from BAlumno import *
from MAlumno import *
from CAlumno import *
from tkinter import *
from tkinter import messagebox

class ABMCAlumno:
    def __init__(self, bd, abierto):
        if abierto:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 432
            h = 110
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
            pantalla.title('ABMC alumno')
            balta = Button(pantalla, height=heigth, width=width, relief="raised", borderwidth=borde,
                           background=colorboton,
                           fg=colorletra, font=fuente, text="Alta Alumno", command=lambda: AAlumno(bd))
            balta.grid(row=0, column=0)
            bbaja = Button(pantalla, height=heigth, width=width, relief="raised", borderwidth=borde,
                           background=colorboton,
                           fg=colorletra, font=fuente, text="Baja Alumno", command=lambda: BAlumno(bd))
            bbaja.grid(row=0, column=1)
            bmodificar = Button(pantalla, height=heigth, width=width, relief="raised", borderwidth=borde,
                                background=colorboton,
                                fg=colorletra, font=fuente, text="Modificar Alumno", command=lambda: MAlumno(bd))
            bmodificar.grid(row=1, column=0)
            bconsulta = Button(pantalla, height=heigth, width=width, relief="raised", borderwidth=borde,
                               background=colorboton,
                               fg=colorletra, font=fuente, text="Consultar Alumno", command=lambda: CAlumno(bd))
            bconsulta.grid(row=1, column=1)
            pantalla.mainloop()
        else:
            messagebox.showwarning("Advertencia", "No ha iniciado la sesion de trabajo.")
