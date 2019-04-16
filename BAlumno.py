from tkinter import *
from tkinter import messagebox

class BAlumno:
    def __init__(self, bd):
        self.__bd = bd
        if self.__bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            self.__pantalla = Toplevel()
            self.__pantalla.grab_set()
            self.__pantalla.resizable(0, 0)
            w = 250
            h = 100
            ws = self.__pantalla.winfo_screenwidth()
            hs = self.__pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            colorboton = "#000000"
            colorletra = "#d35400"
            fuente = "Helvetica 9"
            borde = 5
            self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.__pantalla.title('Baja alumno')
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_Alu")
            lIngrese.grid(padx=10, pady=10, row=0, column=0)
            self.tfcod_alu = Entry(self.__pantalla)
            self.tfcod_alu.grid(row=0, column=1)
            bconsulta = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra,
                               background=colorboton, font=fuente, text="Eliminar", command=self.bajaAlumno)
            bconsulta.grid(row=1, column=1, sticky="w")
            self.__pantalla.mainloop()

    def bajaAlumno(self):
        try:
            cod_alu = int(self.tfcod_alu.get())
            alumno = self.__bd.getAlumno(cod_alu)
            if alumno:
                if not self.__bd.estaDadoDeBaja(cod_alu):
                    if messagebox.askokcancel("Eliminar", "¿Esta seguro que desea eliminar a " + alumno.getNombre()
                                                          + " de la BD?"):
                        self.__bd.bajaAlumno(cod_alu)
                        messagebox.showinfo("Exito", "Alumno eliminado de la BD.")
                        self.__pantalla.destroy()
                else:
                    messagebox.showwarning("Advertencia", "El alumno ya habia sido de baja anteriormente.")
            else:
                messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
        except ValueError:
            messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
