from tkinter import *
from tkinter import messagebox

class CMat:
    def __init__(self, bd):
        self.__bd = bd
        if self.__bd.isEmptyMateria():
            messagebox.showwarning("Advertencia", "No hay materias cargadas en la BD.")
        else:
            self.__pantalla = Toplevel()
            self.__pantalla.grab_set()
            self.__pantalla.resizable(0, 0)
            w = 420
            h = 150
            ws = self.__pantalla.winfo_screenwidth()
            hs = self.__pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            colorboton = "#000000"
            colorletra = "#d35400"
            fuente = "Helvetica 9"
            borde = 5
            self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.__pantalla.title('Consultar Materia')
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_alu")
            lIngrese.grid(padx=10, pady=10, row=0, column=0)
            self.__tfcodalu = Entry(self.__pantalla)
            self.__tfcodalu.grid(row=0, column=1)
            lIngrese2 = Label(self.__pantalla, text="Ingrese Cod_materia")
            lIngrese2.grid(padx=10, row=1, column=0)
            self.__tfcodmat = Entry(self.__pantalla)
            self.__tfcodmat.grid(row=1, column=1)
            self.__bconsulta = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra,
                                      background=colorboton, font=fuente, text="Consultar", command=self.consultaAlumno)
            self.__bconsulta.grid(padx=10, pady=10, row=0, column=2, sticky="w")
            self.__lNombreA = Label(self.__pantalla)
            self.__lNombreM = Label(self.__pantalla)
            self.__lNota = Label(self.__pantalla)
            self.__lNombreA.grid(row=4, column=1)
            self.__lNombreM.grid(row=5, column=1)
            self.__lNota.grid(row=6, column=1)
            self.__pantalla.mainloop()

    def consultaAlumno(self):
        self.__lNombreA.config(text='')
        self.__lNombreM.config(text='')
        self.__lNota.config(text='')
        entradaCorrecta = True
        try:
            codigoMateria = int(self.__tfcodmat.get())
        except ValueError:
            entradaCorrecta = False
        if not entradaCorrecta or codigoMateria < 1 or codigoMateria > 9:
            messagebox.showwarning("Advertencia", "No existe una materia con el codigo ingresado.")
        else:
            try:
                cod_alu = int(self.__tfcodalu.get())
                alumno = self.__bd.getAlumno(cod_alu)
                if alumno:
                    materia = alumno.getMaterias()[codigoMateria-1]
                    self.__lNombreA.config(text="Nombre alumno: " + alumno.getNombre())
                    self.__lNombreM.config(text="Nombre materia: " + materia.getNombre())
                    self.__lNota.config(text="Notas: " + str(materia.getNotas()))
                else:
                    messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
            except ValueError:
                messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
