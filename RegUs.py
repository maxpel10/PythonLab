from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class RegUs:
    def __init__(self, bd, abierto):
        if abierto:
            self.__bd = bd
            self.__pantalla = Toplevel()
            self.__pantalla.resizable(0, 0)
            self.__pantalla.grab_set()
            w = 300
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
            self.__pantalla.title('Registrar Usuario')
            self.__acceso = Label(self.__pantalla, text="Tipo de acceso", font=fuente)
            self.__acceso.grid(pady=10, padx=10, row=0, column=0)
            self.__combo = ttk.Combobox(self.__pantalla, state='readonly')
            self.__combo["values"] = ["Administrador", "Alumno", "Docente"]
            self.__combo.set("Administrador")
            self.__combo.grid(pady=10, padx=10, row=0, column=1, columnspan=2)
            lusuario = Label(self.__pantalla, text="Usuario", font=fuente)
            lusuario.grid(row=1, column=0)
            self.__tfusuario = Entry(self.__pantalla)
            self.__tfusuario.grid(row=1, column=1)
            lcontrasena = Label(self.__pantalla, text="Contraseña", font=fuente)
            lcontrasena.grid(pady=10, padx=10, row=2, column=0)
            self.__tfcontrasena = Entry(self.__pantalla, show="*")
            self.__tfcontrasena.grid(pady=10, padx=10, row=2, column=1)
            bregistrar = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra,
                                background=colorboton, font=fuente, text="Registrar",
                                command=self.altaUsuario)
            bregistrar.grid(row=3, column=1)
            self.__pantalla.mainloop()
        else:
            messagebox.showwarning("Advertencia", "No ha iniciado la sesion de trabajo.")

    def altaUsuario(self):
        user = self.__tfusuario.get()
        password = self.__tfcontrasena.get()
        estaBien = True
        if user == "" or password == "":
            messagebox.showwarning("Advertencia", "El usuario y/o la contraseña ingresada es vacia.")
            estaBien = False
        if self.__bd.existeUsuario(self.__tfusuario.get()) and estaBien:
            messagebox.showwarning("Advertencia", "El usuario ingresado ya existe en la BD.")
            estaBien = False

        if estaBien:
            self.__acceso = self.__combo.get()
            if self.__acceso == "Administrador":
                user = "P-" + user
            elif self.__acceso == "Alumno":
                user = "A-" + user
            else:
                user = "D-" + user
            self.__bd.altaUsuario(user, password)
            messagebox.showinfo("Exito", "El usuario fue ingresado a la BD.")
            self.__pantalla.destroy()
