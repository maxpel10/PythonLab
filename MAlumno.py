from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Alumno import *


def validarFecha(dia, mes, ano):
    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        return dia, mes, ano
    except ValueError:
        return False


class MAlumno:
    def __init__(self, bd):
        self.__bd = bd
        self.__alumno = ""
        if self.__bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            self.__pantalla = Toplevel()
            self.__pantalla.grab_set()
            self.__pantalla.resizable(0, 0)
            w = 370
            h = 475
            ws = self.__pantalla.winfo_screenwidth()
            hs = self.__pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            self.__colorboton = "#000000"
            self.__colorletra = "#d35400"
            self.__fuente = "Helvetica 9"
            self.__borde = 5
            self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.__pantalla.title('Modificar alumno')
            lIngrese = Label(self.__pantalla, text="Ingrese Cod_Alu")
            lIngrese.grid(row=0, column=0, padx=10)
            self.__tfcod_alu = Entry(self.__pantalla)
            self.__tfcod_alu.grid(row=0, column=1, columnspan=3)
            bconsulta = Button(self.__pantalla, relief="raised", borderwidth=self.__borde, fg=self.__colorletra,
                               background=self.__colorboton, font=self.__fuente, text="Consultar",
                               command=self.cargarAlumno)
            bconsulta.grid(row=0, column=5, padx=10)
            self.__lnombre = Label(self.__pantalla, text="Nombre")
            self.__ldni = Label(self.__pantalla, text="DNI")
            self.__ldireccion = Label(self.__pantalla, text="Direccion")
            self.__ltelefono = Label(self.__pantalla, text="Telefono")
            self.__lemail = Label(self.__pantalla, text="Email")
            self.__lfechanacimiento = Label(self.__pantalla, text="Fecha de Nacimiento")
            self.__lcurso = Label(self.__pantalla, text="Curso")
            self.__lfechaalta = Label(self.__pantalla, text="Fecha Alta")
            self.__lfechabaja = Label(self.__pantalla, text="Fecha Baja(opcional)")
            self.__lconcepto = Label(self.__pantalla, text="Concepto")
            self.__linasistencias = Label(self.__pantalla, text="Inasistencias")
            self.__lusuario = Label(self.__pantalla, text="Usuario")
            self.__lcontrasena = Label(self.__pantalla, text="Contraseña")
            self.__tfnombre = Entry(self.__pantalla)
            self.__tfdni = Entry(self.__pantalla)
            self.__tfdireccion = Entry(self.__pantalla)
            self.__tftelefono = Entry(self.__pantalla)
            self.__tfemail = Entry(self.__pantalla)
            self.__dn = Entry(self.__pantalla, width=3)
            self.__mn = Entry(self.__pantalla, width=3)
            self.__an = Entry(self.__pantalla, width=5)
            self.__tfcurso = Entry(self.__pantalla)
            self.__da = Entry(self.__pantalla, width=3)
            self.__ma = Entry(self.__pantalla, width=3)
            self.__tfconcepto = ttk.Combobox(self.__pantalla, state='readonly', width=16)
            self.__tfconcepto["values"] = ["MA", "A", "NA"]
            self.__aa = Entry(self.__pantalla, width=5)
            self.__db = Entry(self.__pantalla, width=3)
            self.__mb = Entry(self.__pantalla, width=3)
            self.__ab = Entry(self.__pantalla, width=5)
            self.__tfinasistencias = Entry(self.__pantalla)
            self.__tfusuario = Entry(self.__pantalla)
            self.__tfcontrasena = Entry(self.__pantalla)
            self.__pantalla.mainloop()

    def cargarAlumno(self):
        try:
            cod_alu = int(self.__tfcod_alu.get())
            self.__alumno = self.__bd.getAlumno(cod_alu)
            self.__tfnombre.delete(0, END)
            self.__tfdni.delete(0, END)
            self.__tfdireccion.delete(0, END)
            self.__tftelefono.delete(0, END)
            self.__tfemail.delete(0, END)
            self.__dn.delete(0, END)
            self.__mn.delete(0, END)
            self.__an.delete(0, END)
            self.__tfcurso.delete(0, END)
            self.__da.delete(0, END)
            self.__ma.delete(0, END)
            self.__aa.delete(0, END)
            self.__db.delete(0, END)
            self.__mb.delete(0, END)
            self.__ab.delete(0, END)
            self.__tfconcepto.set("MA")
            self.__tfinasistencias.delete(0, END)
            self.__tfusuario.delete(0, END)
            self.__tfcontrasena.delete(0, END)
            if self.__alumno:
                self.__tfnombre.insert(0, self.__alumno.getNombre())
                self.__tfdni.insert(0, str(self.__alumno.getDNI()))
                self.__tfdireccion.insert(0, self.__alumno.getDireccion())
                self.__tftelefono.insert(0, str(self.__alumno.getTelefono()))
                self.__tfemail.insert(0, self.__alumno.getEmail())
                f = self.__alumno.getFechaNacimiento()
                self.__dn.insert(0, str(f[0]))
                self.__mn.insert(0, str(f[1]))
                self.__an.insert(0, str(f[2]))
                self.__tfcurso.insert(0, str(self.__alumno.getCurso()))
                f = self.__alumno.getFechaAlta()
                self.__da.insert(0, f[0])
                self.__ma.insert(0, str(f[1]))
                self.__aa.insert(0, str(f[2]))
                f = self.__alumno.getFechaBaja()
                self.__db.insert(0, str(f[0]))
                self.__mb.insert(0, str(f[1]))
                self.__ab.insert(0, str(f[2]))
                self.__tfconcepto.set(self.__alumno.getConcepto())
                self.__tfinasistencias.insert(0, str(self.__alumno.getInasistencias()))
                self.__tfusuario.insert(0, self.__alumno.getUsuario()[2:])
                self.__tfcontrasena.insert(0, self.__alumno.getContrasena())
                self.__lnombre.grid(pady=5, row=1, column=0, sticky="w", padx=10)
                self.__ldni.grid(pady=5, row=2, column=0, sticky="w", padx=10)
                self.__ldireccion.grid(pady=5, row=3, column=0, sticky="w", padx=10)
                self.__ltelefono.grid(pady=5, row=4, column=0, sticky="w", padx=10)
                self.__lemail.grid(pady=5, row=5, column=0, sticky="w", padx=10)
                self.__lfechanacimiento.grid(pady=6, row=6, column=0, sticky="w", padx=10)
                self.__lcurso.grid(pady=5, row=7, column=0, sticky="w", padx=10)
                self.__lfechaalta.grid(pady=5, row=8, column=0, sticky="w", padx=10)
                self.__lfechabaja.grid(pady=5, row=9, column=0, sticky="w", padx=10)
                self.__lconcepto.grid(pady=5, row=10, column=0, sticky="w", padx=10)
                self.__linasistencias.grid(pady=5, row=11, column=0, sticky="w", padx=10)
                self.__lusuario.grid(pady=5, row=12, column=0, sticky="w", padx=10)
                self.__lcontrasena.grid(pady=5, row=13, column=0, sticky="w", padx=10)
                self.__tfnombre.grid(pady=5, row=1, column=1, columnspan=3)
                self.__tfdni.grid(pady=5, row=2, column=1, columnspan=3)
                self.__tfdireccion.grid(pady=5, row=3, column=1, columnspan=3)
                self.__tftelefono.grid(pady=5, row=4, column=1, columnspan=3)
                self.__tfemail.grid(pady=5, row=5, column=1, columnspan=3)
                self.__dn.grid(row=6, column=1, sticky="e")
                self.__mn.grid(row=6, column=2)
                self.__an.grid(row=6, column=3, sticky="w")
                self.__tfcurso.grid(pady=5, row=7, column=1, columnspan=3)
                self.__da.grid(row=8, column=1, sticky="e")
                self.__ma.grid(row=8, column=2)
                self.__aa.grid(row=8, column=3, sticky="w")
                self.__db.grid(row=9, column=1, sticky="e")
                self.__mb.grid(row=9, column=2)
                self.__ab.grid(row=9, column=3, sticky="w")
                self.__tfconcepto.grid(pady=5, row=10, column=1, columnspan=3)
                self.__tfinasistencias.grid(pady=5, row=11, column=1, columnspan=3)
                self.__tfusuario.grid(pady=5, row=12, column=1, columnspan=3)
                self.__tfcontrasena.grid(pady=5, row=13, column=1, columnspan=3)
                bmodificar = Button(self.__pantalla,  relief="raised", borderwidth=self.__borde, fg=self.__colorletra,
                                    background=self.__colorboton, font=self.__fuente, text="Modificar",
                                    command=self.modificarAlumno)
                bmodificar.grid(row=15, padx=10, column=1, columnspan=3)
            else:
                messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")
        except ValueError:
            messagebox.showwarning("Advertencia", "No existe un alumno con el codigo ingresado.")

    def modificarAlumno(self):
        nroRegistro = int(self.__tfcod_alu.get())
        nombre = self.__tfnombre.get()
        dni = self.__tfdni.get()
        direccion = self.__tfdireccion.get()
        telefono = self.__tftelefono.get()
        email = self.__tfemail.get()
        dn = self.__dn.get()
        mn = self.__mn.get()
        an = self.__an.get()
        curso = self.__tfcurso.get()
        da = self.__da.get()
        ma = self.__ma.get()
        aa = self.__aa.get()
        db = self.__db.get()
        mb = self.__mb.get()
        ab = self.__ab.get()
        concepto = self.__tfconcepto.get()
        inasistencias = self.__tfinasistencias.get()
        usuario = "A-"+self.__tfusuario.get()
        contrasena = self.__tfcontrasena.get()

        estaBien = True
        if nombre == "" or dni == "" or direccion == "" or telefono == "" or dn == "" or mn == "" or an == "" or \
                email == "" or curso == "" or da == "" or ma == "" or aa == "" or inasistencias == "" or \
                usuario == "" or contrasena == "":
            estaBien = False
            messagebox.showwarning("Advertencia", "Los campos no opcionales no pueden estar vacios.")

        if estaBien and not re.match(r'[a-zA-Z\s]+$', nombre):
            estaBien = False
            messagebox.showwarning("Advertencia", "El nombre contiene caracteres invalidos.")

        if estaBien:
            try:
                dni = int(dni)
            except ValueError:
                estaBien = False
                messagebox.showwarning("Advertencia", "El dni contiene caracteres invalidos.")

        if estaBien and self.__bd.existeDNI(dni) and dni != self.__alumno.getDNI():
            estaBien = False
            messagebox.showwarning("Advertencia", "Ya existe un alumno con el dni ingresado.")

        if estaBien:
            try:
                telefono = int(telefono)
            except ValueError:
                estaBien = False
                messagebox.showwarning("Advertencia", "El telefono contiene caracteres invalidos.")

        if estaBien and not re.match('^[(a-z0-9_\-.)]+@[(a-z0-9_\-.)]+\.[(a-z)]{2,15}$', email.lower()):
            estaBien = False
            messagebox.showwarning("Advertencia", "Formato de email incorrecto.")

        fechaNacimiento = validarFecha(dn, mn, an)
        if estaBien and not fechaNacimiento:
            estaBien = False
            messagebox.showwarning("Advertencia", "Formato de de fecha de nacimiento incorrecto.")

        if estaBien:
            try:
                curso = int(curso)
            except ValueError:
                estaBien = False
                messagebox.showwarning("Advertencia", "El curso contiene caracteres invalidos.")

        fechaAlta = validarFecha(da, ma, aa)
        if estaBien and not fechaAlta:
            estaBien = False
            messagebox.showwarning("Advertencia", "Formato de de fecha de alta incorrecto.")

        if db == "" and mb == "" and ab == "":
            fechaBaja = (0, 0, 0)
        else:
            fechaBaja = validarFecha(db, mb, ab)
            if estaBien and not fechaBaja:
                estaBien = False
                messagebox.showwarning("Advertencia", "Formato de de fecha de baja incorrecto.")

        if estaBien:
            try:
                inasistencias = int(inasistencias)
            except ValueError:
                estaBien = False
                messagebox.showwarning("Advertencia", "Las inasistencias contienen caracteres invalidos.")

        if estaBien and self.__bd.existeUsuario(usuario) and usuario != self.__alumno.getUsuario():
            estaBien = False
            messagebox.showwarning("Advertencia", "El usuario ingresado ya existe.")

        if estaBien and nombre == self.__alumno.getNombre() and dni == self.__alumno.getDNI() and \
                direccion == self.__alumno.getDireccion() and telefono == self.__alumno.getTelefono() and \
                email == self.__alumno.getEmail() and fechaNacimiento == self.__alumno.getFechaNacimiento() and \
                curso == self.__alumno.getCurso() and fechaAlta == self.__alumno.getFechaAlta() and \
                fechaBaja == self.__alumno.getFechaBaja() and concepto == self.__alumno.getConcepto() and\
                inasistencias == self.__alumno.getInasistencias() and usuario == self.__alumno.getUsuario() and\
                contrasena == self.__alumno.getContrasena():
            estaBien = False
            messagebox.showwarning("Advertencia", "No se ha modificado ningun campo.")

        if estaBien:
            alumno = Alumno(nroRegistro, nombre, dni, direccion, telefono, email, fechaNacimiento, curso, fechaAlta,
                            fechaBaja, concepto, inasistencias, [], usuario, contrasena)
            self.__bd.modificarAlumno(alumno, self.__alumno.getUsuario())
            messagebox.showinfo("Exito", "Modificación realizada.")
            self.__pantalla.destroy()
