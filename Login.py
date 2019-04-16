from PantallaPrincipalAdm import *
from PantallaPrincipalGral import *
from BD_Escuela import *
from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, bd):
        self.__bd = bd
        if not self.__bd.leerArchivo():
            messagebox.showerror("Error", "No se ha encontrado BD.txt")
        self.__login = Tk()
        w = 230
        h = 115
        colorboton = "#000000"
        colorletra = "#d35400"
        fuente = "Helvetica 9"
        borde = 5
        ws = self.__login.winfo_screenwidth()
        hs = self.__login.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__login.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__login.resizable(0, 0)
        self.__login.title('Login')
        self.__lusuario = Label(self.__login, text="Usuario", font=fuente)
        self.__lusuario.grid(pady=10, padx=10, row=0, column=0, columnspan=2)
        self.__tfusuario = Entry(self.__login)
        self.__tfusuario.grid(pady=10, row=0, column=2, columnspan=2)
        self.__lcontrasena = Label(self.__login, text="Contraseña", font=fuente)
        self.__lcontrasena.grid(padx=10, row=1, column=0, columnspan=2)
        self.__tfcontrasena = Entry(self.__login, show="*")
        self.__tfcontrasena.grid(row=1, column=2, columnspan=2)
        bingresar = Button(self.__login, relief="raised", borderwidth=borde, background=colorboton, fg=colorletra,
                           font=fuente, text="Ingresar", command=self.validarIngreso)
        bingresar.grid(pady=10, row=2, column=1, columnspan=2)
        bsalir = Button(self.__login, relief="raised", borderwidth=borde, background=colorboton, fg=colorletra,
                        font=fuente, text="Salir", command=quit)
        bsalir.grid(pady=10, row=2, column=2, columnspan=2)
        self.__login.mainloop()

    def validarIngreso(self):
        acceso = self.__bd.validarIngreso(self.__tfusuario.get(), self.__tfcontrasena.get())
        if acceso == 1:
            PantallaPrincipalAdm(self.__login, self.__bd)
        elif acceso == 2 or acceso == 3:
            PantallaPrincipalGral(self.__login, self.__bd)
        else:
            messagebox.showwarning("Advertencia", "Usuario y/o contraseña incorrectos.")


baseDeDatos = BD_Escuela()
Login(baseDeDatos)
