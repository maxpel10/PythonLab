from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class ElimUs:
    def __init__(self, bd, abierto):
        if abierto:
            self.__bd = bd
            self.__listaUsuarios = self.__bd.getListaUsuarios()
            if self.__listaUsuarios:
                self.__pantalla = Toplevel()
                self.__pantalla.grab_set()
                self.__pantalla.resizable(0, 0)
                w = 300
                h = 100
                ws = self.__pantalla.winfo_screenwidth()
                hs = self.__pantalla.winfo_screenheight()
                x = (ws / 2) - (w / 2)
                y = (hs / 2) - (h / 2)
                self.__pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
                colorboton = "#000000"
                colorletra = "#d35400"
                fuente = "Helvetica 9"
                borde = 5
                self.__pantalla.title('Eliminar Usuario')
                lInfo = Label(self.__pantalla, text="Usuario a eliminar", font=fuente)
                lInfo.grid(pady=10, padx=10, row=0, column=0)
                self.__combo = ttk.Combobox(self.__pantalla, state='readonly')
                self.__combo["values"] = self.__listaUsuarios
                self.__combo.set(self.__listaUsuarios[0])
                self.__combo.grid(pady=10, padx=10, row=0, column=1, columnspan=2)
                self.__beliminar = Button(self.__pantalla, relief="raised", borderwidth=borde, fg=colorletra, background=colorboton, font=fuente, text="Eliminar", command=self.bajaUsuario)
                self.__beliminar.grid(row=3, column=1)
                self.__pantalla.mainloop()
            else:
                messagebox.showwarning("Advertencia", "No hay usuarios cargados en la BD.")
        else:
            messagebox.showwarning("Advertencia", "No ha iniciado la sesion de trabajo.")

    def bajaUsuario(self):
        self.__bd.bajaUsuario(self.__combo.get())
        messagebox.showinfo("Exito", "El usuario fue eliminado de la BD.")
        self.__pantalla.destroy()
