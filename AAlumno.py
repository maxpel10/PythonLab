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


class AAlumno:
    def __init__(self, bd):
        self.__bd = bd
        self.__pantalla = Toplevel()
        self.__pantalla.grab_set()
        self.__pantalla.resizable(0, 0)
        w = 300
        h = 450
        ws = self.__pantalla.winfo_screenwidth()
        hs = self.__pantalla.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        colorboton = "#000000"
        colorletra = "#d35400"
        fuente = "Helvetica 9"
        borde = 5
        self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__pantalla.title('Alta alumno')
        lnombre = Label(self.__pantalla, text="Nombre")
        lnombre.grid(pady=5, padx=10, row=0, column=0, sticky="w")
        ldni = Label(self.__pantalla, text="DNI")
        ldni.grid(pady=5, padx=10, row=1, column=0, sticky="w")
        ldireccion = Label(self.__pantalla, text="Direccion")
        ldireccion.grid(pady=5, padx=10, row=2, column=0, sticky="w")
        ltelefono = Label(self.__pantalla, text="Telefono")
        ltelefono.grid(pady=5, padx=10, row=3, column=0, sticky="w")
        lemail = Label(self.__pantalla, text="Email")
        lemail.grid(pady=5, padx=10, row=4, column=0, sticky="w")
        lfechanacimiento = Label(self.__pantalla, text="Fecha de Nacimiento")
        lfechanacimiento.grid(pady=5, padx=10, row=5, column=0, sticky="w")
        lcurso = Label(self.__pantalla, text="Curso")
        lcurso.grid(pady=5, padx=10, row=6, column=0, sticky="w")
        lfechaalta = Label(self.__pantalla, text="Fecha Alta")
        lfechaalta.grid(pady=5, padx=10, row=7, column=0, sticky="w")
        lfechabaja = Label(self.__pantalla, text="Fecha Baja(opcional)")
        lfechabaja.grid(pady=5, padx=10, row=8, column=0, sticky="w")
        lconcepto = Label(self.__pantalla, text="Concepto")
        lconcepto.grid(pady=5, padx=10, row=9, column=0, sticky="w")
        linasistencias = Label(self.__pantalla, text="Inasistencias")
        linasistencias.grid(pady=5, padx=10, row=10, column=0, sticky="w")
        lusuario = Label(self.__pantalla, text="Usuario")
        lusuario.grid(pady=5, padx=10, row=11, column=0, sticky="w")
        lcontrasena = Label(self.__pantalla, text="Contraseña")
        lcontrasena.grid(pady=5, padx=10,  row=12, column=0, sticky="w")
        self.__tfnombre = Entry(self.__pantalla)
        self.__tfnombre.grid(pady=5, row=0, column=1, columnspan=3)
        self.__tfdni = Entry(self.__pantalla)
        self.__tfdni.grid(pady=5, row=1, column=1, columnspan=3)
        self.__tfdireccion = Entry(self.__pantalla)
        self.__tfdireccion.grid(pady=5, row=2, column=1, columnspan=3)
        self.__tftelefono = Entry(self.__pantalla)
        self.__tftelefono.grid(pady=5, row=3, column=1, columnspan=3)
        self.__tfemail = Entry(self.__pantalla)
        self.__tfemail.grid(pady=5, row=4, column=1, columnspan=3)
        self.__dn = Entry(self.__pantalla, width=3)
        self.__dn.grid(row=5, column=1, sticky="e")
        self.__mn = Entry(self.__pantalla, width=3)
        self.__mn.grid(row=5, column=2)
        self.__an = Entry(self.__pantalla, width=5)
        self.__an.grid(row=5, column=3, sticky="w")
        self.__tfcurso = Entry(self.__pantalla)
        self.__tfcurso.grid(pady=5, row=6, column=1, columnspan=3)
        self.__da = Entry(self.__pantalla, width=3)
        self.__da.grid(row=7, column=1, sticky="e")
        self.__ma = Entry(self.__pantalla, width=3)
        self.__ma.grid(row=7, column=2)
        self.__aa = Entry(self.__pantalla, width=5)
        self.__aa.grid(row=7, column=3, sticky="w")
        self.__db = Entry(self.__pantalla, width=3)
        self.__db.grid(row=8, column=1, sticky="e")
        self.__mb = Entry(self.__pantalla, width=3)
        self.__mb.grid(row=8, column=2)
        self.__ab = Entry(self.__pantalla, width=5)
        self.__ab.grid(row=8, column=3, sticky="w")
        self.__tfconcepto = ttk.Combobox(self.__pantalla, state='readonly', width=16)
        self.__tfconcepto["values"] = ["MA", "A", "NA"]
        self.__tfconcepto.set("MA")
        self.__tfconcepto.grid(pady=5, row=9, column=1, columnspan=3)
        self.__tfinasistencias = Entry(self.__pantalla)
        self.__tfinasistencias.grid(pady=5, row=10, column=1, columnspan=3)
        self.__tfusuario = Entry(self.__pantalla)
        self.__tfusuario.grid(pady=5, row=11, column=1, columnspan=3)
        self.__tfcontrasena = Entry(self.__pantalla)
        self.__tfcontrasena.grid(pady=5, row=12, column=1, columnspan=3)
        bdardealta = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra, background=colorboton,
                            font=fuente, text="Dar de alta", width=16, command=self.altaAlumno)
        bdardealta.grid(row=14, padx=10, column=1, columnspan=3)

    def altaAlumno(self):
        nroRegistro = self.__bd.getMaximoNroRegistro()+1
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
        usuario = self.__tfusuario.get()
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

        if estaBien and self.__bd.existeDNI(dni):
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

        if estaBien and self.__bd.existeUsuario(usuario):
            estaBien = False
            messagebox.showwarning("Advertencia", "El usuario ingresado ya existe.")

        if estaBien:
            alumno = Alumno(nroRegistro, nombre, dni, direccion, telefono, email, fechaNacimiento, curso, fechaAlta,
                            fechaBaja, concepto, inasistencias, [], "A-"+usuario, contrasena)
            self.__bd.altaAlumno(alumno)
            messagebox.showinfo("Exito", "Alumno ingresado a la BD.")
            self.__pantalla.destroy()
