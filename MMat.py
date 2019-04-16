from tkinter import *
from tkinter import messagebox

from Materia import Materia


class MMat:
    def __init__(self, bd):
        self.__bd = bd
        self.__alumno = ""
        if self.__bd.isEmptyMateria():
            messagebox.showwarning("Advertencia", "No hay materias cargadas en la BD.")
        else:
            self.__pantalla = Toplevel()
            self.__pantalla.grab_set()
            self.__pantalla.resizable(0, 0)
            w = 370
            h = 200
            ws = self.__pantalla.winfo_screenwidth()
            hs = self.__pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            self.__colorboton = "#000000"
            self.__colorletra = "#d35400"
            self.__fuente = "Helvetica 9"
            self.__borde = 5
            self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.__pantalla.title('Modificar materia')
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_Alu")
            lIngrese.grid(row=0, column=0, padx=10)
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_alu")
            lIngrese.grid(padx=10, pady=10, row=0, column=0)
            self.__tfcodalu = Entry(self.__pantalla)
            self.__tfcodalu.grid(row=0, column=1)
            lIngrese2 = Label(self.__pantalla, text="Ingrese Cod_materia")
            lIngrese2.grid(padx=10, row=1, column=0)
            self.__tfcodmat = Entry(self.__pantalla)
            self.__tfcodmat.grid(row=1, column=1)
            self.__bconsulta = Button(self.__pantalla, relief="raised", borderwidth=self.__borde, fg=self.__colorletra,
                                      background=self.__colorboton, font=self.__fuente, text="Consultar",
                                      command=self.cargarMateria)
            self.__bconsulta.grid(padx=10, pady=10, row=0, column=2, sticky="w")
            self.__lnota1 = Label(self.__pantalla, text="Nota 1C")
            self.__lnota2 = Label(self.__pantalla, text="Nota 2C")
            self.__lnota3 = Label(self.__pantalla, text="Nota 3C")
            self.__tfnota1 = Entry(self.__pantalla)
            self.__tfnota2 = Entry(self.__pantalla)
            self.__tfnota3 = Entry(self.__pantalla)
            self.__pantalla.mainloop()

    def cargarMateria(self):
        entradaCorrecta = True
        codigoMateria = 0
        try:
            codigoMateria = int(self.__tfcodmat.get())
        except ValueError:
            entradaCorrecta = False
        if not entradaCorrecta or codigoMateria < 1 or codigoMateria > 9:
            messagebox.showwarning("Advertencia", "No existe una materia con el codigo ingresado.")
        else:
            try:
                cod_alu = int(self.__tfcodalu.get())
                self.__alumno = self.__bd.getAlumno(cod_alu)
                self.__tfnota1.delete(0, END)
                self.__tfnota2.delete(0, END)
                self.__tfnota3.delete(0, END)
                if self.__alumno:
                    materia = self.__alumno.getMaterias()[codigoMateria-1]
                    notas = materia.getNotas()
                    self.__tfnota1.insert(0, notas[0])
                    self.__tfnota2.insert(0, notas[1])
                    self.__tfnota3.insert(0, notas[2])
                    self.__lnota1.grid(pady=5, row=2, column=0, sticky="w", padx=10)
                    self.__lnota2.grid(pady=5, row=3, column=0, sticky="w", padx=10)
                    self.__lnota3.grid(pady=5, row=4, column=0, sticky="w", padx=10)
                    self.__tfnota1.grid(pady=5, row=2, column=1, sticky="w", padx=10)
                    self.__tfnota2.grid(pady=5, row=3, column=1, sticky="w", padx=10)
                    self.__tfnota3.grid(pady=5, row=4, column=1, sticky="w", padx=10)
                    bmodificar = Button(self.__pantalla, relief="raised", borderwidth=self.__borde,
                                        fg=self.__colorletra,
                                        background=self.__colorboton, font=self.__fuente, text="Modificar",
                                        command=self.modificarMateria)
                    bmodificar.grid(row=5, padx=10, column=1, columnspan=3, sticky="w")
                else:
                    messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
            except ValueError:
                messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")

    def modificarMateria(self):
        nota1 = self.__tfnota1.get()
        nota2 = self.__tfnota2.get()
        nota3 = self.__tfnota3.get()

        estaBien = True

        if estaBien:
            try:
                nota1 = int(nota1)
                nota2 = int(nota2)
                nota3 = int(nota3)
            except ValueError:
                estaBien = False
                messagebox.showwarning("Advertencia", "Los campos contienen al menos un caracter invalido.")

        codigoMateria = int(self.__tfcodmat.get())
        materia = self.__alumno.getMaterias()[codigoMateria - 1]
        notas = materia.getNotas()
        if estaBien and nota1 == notas[0] and nota2 == notas[1] and nota3 == notas[2]:
            estaBien = False
            messagebox.showwarning("Advertencia", "No se ha modificado ningun campo.")

        if estaBien:
            cod_alu = int(self.__tfcodalu.get())
            materiaa = Materia(codigoMateria, cod_alu, materia.getNombre(),(nota1, nota2, nota3))
            self.__bd.modificarMateria(materiaa)
            messagebox.showinfo("Exito", "Modificación realizada.")
            self.__pantalla.destroy()
