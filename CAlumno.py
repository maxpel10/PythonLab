from tkinter import *
from tkinter import messagebox

class CAlumno:
    def __init__(self, bd):
        self.__bd = bd
        if self.__bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            self.__pantalla = Toplevel()
            self.__pantalla.grab_set()
            self.__pantalla.resizable(0, 0)
            w = 380
            h = 320
            ws = self.__pantalla.winfo_screenwidth()
            hs = self.__pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            colorboton = "#000000"
            colorletra = "#d35400"
            fuente = "Helvetica 9"
            borde = 5
            self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.__pantalla.title('Consultar Alumno')
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_alu")
            lIngrese.grid(padx=10, pady=10, row=0, column=0)
            self.__tfcodalu = Entry(self.__pantalla)
            self.__tfcodalu.grid(row=0, column=1)
            self.__bconsulta = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra,
                                      background=colorboton, font=fuente, text="Consultar", command=self.consultaAlumno)
            self.__bconsulta.grid(padx=10, pady=10, row=0, column=2)
            self.__lNombre = Label(self.__pantalla)
            self.__lDni = Label(self.__pantalla)
            self.__lDireccion = Label(self.__pantalla)
            self.__lTelefono = Label(self.__pantalla)
            self.__lFechaNacimiento = Label(self.__pantalla)
            self.__lCurso = Label(self.__pantalla)
            self.__lFechaAlta = Label(self.__pantalla)
            self.__lFechaBaja = Label(self.__pantalla)
            self.__lConcepto = Label(self.__pantalla)
            self.__lInasistencias = Label(self.__pantalla)
            self.__lUsuario = Label(self.__pantalla)
            self.__lContrasena = Label(self.__pantalla)
            self.__lNombre.grid(row=1, column=1)
            self.__lDni.grid(row=2, column=1)
            self.__lDireccion.grid(row=3, column=1)
            self.__lTelefono.grid(row=4, column=1)
            self.__lCurso.grid(row=5, column=1)
            self.__lFechaNacimiento.grid(row=6, column=1)
            self.__lFechaAlta.grid(row=7, column=1)
            self.__lFechaBaja.grid(row=8, column=1)
            self.__lConcepto.grid(row=9, column=1)
            self.__lInasistencias.grid(row=10, column=1)
            self.__lUsuario.grid(row=11, column=1)
            self.__lContrasena.grid(row=12, column=1)
            self.__pantalla.mainloop()

    def consultaAlumno(self):
        self.__lNombre.config(text='')
        self.__lDni.config(text='')
        self.__lDireccion.config(text='')
        self.__lTelefono.config(text='')
        self.__lFechaNacimiento.config(text='')
        self.__lCurso.config(text='')
        self.__lFechaAlta.config(text='')
        self.__lFechaBaja.config(text='')
        self.__lConcepto.config(text='')
        self.__lInasistencias.config(text='')
        self.__lUsuario.config(text='')
        self.__lContrasena.config(text='')
        try:
            cod_alu = int(self.__tfcodalu.get())
            alumno = self.__bd.getAlumno(cod_alu)
            if alumno:
                self.__lNombre.config(text="Nombre: " + alumno.getNombre())
                self.__lDni.config(text="Dni: " + str(alumno.getDNI()))
                self.__lDireccion.config(text="Direccion: " + alumno.getDireccion())
                self.__lTelefono.config(text="Telefono: " + str(alumno.getTelefono()))
                self.__lFechaNacimiento.config(text="Fecha Nacimiento: " + str(alumno.getFechaNacimiento()))
                self.__lCurso.config(text="Curso: " + str(alumno.getCurso()) + "° año")
                self.__lFechaAlta.config(text="Fecha Alta: " + str(alumno.getFechaAlta()))
                self.__lFechaBaja.config(text="FechaBaja: " + str(alumno.getFechaBaja()))
                self.__lConcepto.config(text="Concepto " + alumno.getConcepto())
                self.__lInasistencias.config(text="Inasistencias: " + str(alumno.getInasistencias()))
                self.__lUsuario.config(text="Usuario: " + alumno.getUsuario())
                self.__lContrasena.config(text="Contraseña: " + alumno.getContrasena())
            else:
                messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
        except ValueError:
            messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
