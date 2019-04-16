from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox
class LisInas:
    def __init__(self, bd):
        if bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 255
            h = 700
            ws = pantalla.winfo_screenwidth()
            hs = pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            pantalla.title('Listar inasistencias')
            listaAlumnos = bd.getAReadmitir()
            listaAlumnos.sort(key=(lambda x: x[0]))
            for r in range(0, len(listaAlumnos)*2+2, 2):
                if r == 0:
                    largo = len(listaAlumnos)*2+2
                    label1 = Label(pantalla, width=20, text="Nombre")
                    label1.grid(row=r, column=0)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=1, sticky="ns", rowspan=largo)
                    label2 = Label(pantalla, width=5, text="Curso")
                    label2.grid(row=r, column=2)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=3, sticky="ns", rowspan=largo)
                    label3 = Label(pantalla, width=8, text="Concepto")
                    label3.grid(row=r, column=4)
                    for i in range(0, 5):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=1, column=i, sticky="we")
                else:
                    alumno = listaAlumnos[int((r-2)/2)]
                    label1 = Label(pantalla, width=20, text=alumno[0])
                    label1.grid(row=r, column=0)
                    label2 = Label(pantalla, width=5, text=str(alumno[1]))
                    label2.grid(row=r, column=2)
                    label3 = Label(pantalla, width=8, text=alumno[2])
                    label3.grid(row=r, column=4)
                    for i in range(0, 5):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=r+1, column=i, sticky="we")
            pantalla.mainloop()
