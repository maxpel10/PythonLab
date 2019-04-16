from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

class LisTAlu:
    def __init__(self, bd):
        if bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 1180
            h = 700
            ws = pantalla.winfo_screenwidth()
            hs = pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            pantalla.title('Listar alumnos')
            listaAlumnos = bd.getListaAlumnos()
            listaAlumnos.sort(key=(lambda x: x.getNroRegistro()))
            for r in range(0, len(listaAlumnos)*2+2, 2):
                if r == 0:
                    largo = len(listaAlumnos)*2+2
                    label1 = Label(pantalla, width=10, text="Nro Registro")
                    label1.grid(row=r, column=0)
                    label2 = Label(pantalla, width=10, text="Nombre")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=1, sticky="ns", rowspan=largo)
                    label2.grid(row=r, column=2)
                    label3 = Label(pantalla, width=10, text="DNI")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=3, sticky="ns", rowspan=largo)
                    label3.grid(row=r, column=4)
                    label4 = Label(pantalla, width=10, text="Direccion")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=5, sticky="ns", rowspan=largo)
                    label4.grid(row=r, column=6)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=7, sticky="ns", rowspan=largo)
                    label5 = Label(pantalla, width=10, text="Telefono")
                    label5.grid(row=r, column=8)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=9, sticky="ns", rowspan=largo)
                    label6 = Label(pantalla, width=10, text="Email")
                    label6.grid(row=r, column=10)
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=11, sticky="ns", rowspan=largo)
                    label7 = Label(pantalla, width=10, text="FechaNac")
                    label7.grid(row=r, column=12)
                    label8 = Label(pantalla, width=10, text="Curso")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=13, sticky="ns", rowspan=largo)
                    label8.grid(row=r, column=14)
                    label9 = Label(pantalla, width=10, text="FechaAlta")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=15, sticky="ns", rowspan=largo)
                    label9.grid(row=r, column=16)
                    label10 = Label(pantalla, width=10, text="FechaBaja")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=17, sticky="ns", rowspan=largo)
                    label10.grid(row=r, column=18)
                    label11 = Label(pantalla, width=10, text="Concepto")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=19, sticky="ns", rowspan=largo)
                    label11.grid(row=r, column=20)
                    label12 = Label(pantalla, width=11, text="Inasistencias")
                    separator = Separator(pantalla, orient="vertical")
                    separator.grid(row=r, column=21, sticky="ns", rowspan=largo)
                    label12.grid(row=r, column=22)
                    for i in range(0, 23):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=1, column=i, sticky="we")
                else:
                    alumno = listaAlumnos[int((r-2)/2)]
                    label1 = Label(pantalla, width=10, text=str(alumno.getNroRegistro()))
                    label1.grid(row=r, column=0)
                    label2 = Label(pantalla, width=20, text=alumno.getNombre())
                    label2.grid(row=r, column=2)
                    label3 = Label(pantalla, width=10, text=str(alumno.getDNI()))
                    label3.grid(row=r, column=4)
                    label4 = Label(pantalla, width=20, text=alumno.getDireccion())
                    label4.grid(row=r, column=6)
                    label5 = Label(pantalla, width=15, text=str(alumno.getTelefono()))
                    label5.grid(row=r, column=8)
                    label6 = Label(pantalla, width=20, text=alumno.getEmail())
                    label6.grid(row=r, column=10)
                    label7 = Label(pantalla, width=10, text=str(alumno.getFechaNacimiento()))
                    label7.grid(row=r, column=12)
                    label8 = Label(pantalla, width=10, text=str(alumno.getCurso()))
                    label8.grid(row=r, column=14)
                    label9 = Label(pantalla, width=10, text=str(alumno.getFechaAlta()))
                    label9.grid(row=r, column=16)
                    label10 = Label(pantalla, width=10, text=str(alumno.getFechaBaja()))
                    label10.grid(row=r, column=18)
                    label11 = Label(pantalla, width=10, text=alumno.getConcepto())
                    label11.grid(row=r, column=20)
                    label12 = Label(pantalla, width=11, text=str(alumno.getInasistencias()))
                    label12.grid(row=r, column=22)
                    for i in range(0, 23):
                        separator = Separator(pantalla, orient="horizontal")
                        separator.grid(row=r+1, column=i, sticky="we")
            pantalla.mainloop()