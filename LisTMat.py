from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

class LisTMat:
    def __init__(self, bd):
        if bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay materias cargadas en la BD.")
        else:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 570
            h = 700
            ws = pantalla.winfo_screenwidth()
            hs = pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            pantalla.title('Listar materias')
            listaMaterias = bd.getListaMaterias()
            listaMaterias.sort(key=(lambda x: x.getCodigoAlumno()))
            for r in range(0, len(listaMaterias)*2+2, 2):
                if r == 0:
                    largo = len(listaMaterias)*2+2
                    label1 = Label(pantalla, width=15, text="Codigo Materia")
                    label1.grid(row=r, column=0)
                    label2 = Label(pantalla, width=15, text="Codigo Alumno")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=1, sticky="ns", rowspan=largo)
                    label2.grid(row=r, column=2)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=3, sticky="ns", rowspan=largo)
                    label3 = Label(pantalla, width=10, text="Nombre")
                    label3.grid(row=r, column=4)
                    label4 = Label(pantalla, width=10, text="Nota 1C")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=5, sticky="ns", rowspan=largo)
                    label4.grid(row=r, column=6)
                    label5 = Label(pantalla, width=10, text="Nota 2C")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=7, sticky="ns", rowspan=largo)
                    label5.grid(row=r, column=8)
                    label6 = Label(pantalla, width=10, text="Nota 3C")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=9, sticky="ns", rowspan=largo)
                    label6.grid(row=r, column=10)
                    for i in range(0, 11):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=r+1, column=i, sticky="we")
                else:
                    materia = listaMaterias[int((r-2)/2)]
                    label1 = Label(pantalla, width=10, text=str(materia.getCodigoMateria()))
                    label1.grid(row=r, column=0)
                    label2 = Label(pantalla, width=10, text=str(materia.getCodigoAlumno()))
                    label2.grid(row=r, column=2)
                    label3 = Label(pantalla, width=15, text=materia.getNombre())
                    label3.grid(row=r, column=4)
                    notas = materia.getNotas()
                    label4 = Label(pantalla, width=10, text=notas[0])
                    label4.grid(row=r, column=6)
                    label5 = Label(pantalla, width=10, text=notas[1])
                    label5.grid(row=r, column=8)
                    label6 = Label(pantalla, width=10, text=notas[2])
                    label6.grid(row=r, column=10)
                    for i in range(0, 11):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=r+1, column=i, sticky="we")
            pantalla.mainloop()
