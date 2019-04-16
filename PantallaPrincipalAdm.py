from ABMCMateria import *
from RegUs import *
from ElimUs import *
from ABMCAlumno import *
from LisInas import *
from LisTAlu import *
from LisTMat import *
from LisLegA import *
from LisRegXCurso import *
from tkinter import *
from tkinter import messagebox


class PantallaPrincipalAdm:
    def __init__(self, login, bd):
        login.destroy()
        self.__abierto = False
        self.__bd = bd
        self.__pp = Tk()
        self.__pp.resizable(0, 0)
        w = 432
        h = 336
        ws = self.__pp.winfo_screenwidth()
        hs = self.__pp.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        width = 20
        heigth = 2
        colorboton = "#000000"
        colorletra = "#d35400"
        fuente = "Helvetica 12 bold italic"
        borde = 5
        self.__pp.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__pp.protocol("WM_DELETE_WINDOW", self.salir)
        self.__pp.title('Menú principal administrador')
        # Funciones de administrador
        bist = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                      fg=colorletra, font=fuente, text="Iniciar sesión de trabajo", command=self.CargaBD)
        bist.grid(row=0, column=0)
        bad = Button(self.__pp, text="Almacenar en disco", height=heigth, width=width, relief="raised", borderwidth=borde,
                     background=colorboton, fg=colorletra, font=fuente, command=self.Backup)
        bad.grid(row=0, column=1)
        bru = Button(self.__pp, text="Registrar usuario", height=heigth, width=width, relief="raised", borderwidth=borde,
                     background=colorboton, fg=colorletra, font=fuente, command=lambda: RegUs(self.__bd, self.__abierto))
        bru.grid(row=1, column=0)
        beu = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Eliminar usuario", command=lambda: ElimUs(self.__bd, self.__abierto))
        beu.grid(row=1, column=1)
        bcruda = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                        fg=colorletra, font=fuente, text="ABMC alumnos",
                        command=lambda: ABMCAlumno(self.__bd, self.__abierto))
        bcruda.grid(row=2, column=0)
        bcrudm = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                        fg=colorletra, font=fuente, text="ABMC materias",
                        command=lambda: ABMCMateria(self.__bd, self.__abierto))
        bcrudm.grid(row=2, column=1)
        # Funciones generales
        bla = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Listar alumnos", command=lambda: LisTAlu(self.__bd))
        bla.grid(row=3, column=0)
        blm = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Listar materias", command=lambda: LisTMat(self.__bd))
        blm.grid(row=3, column=1)
        bll = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Listar legajo alumno", command=lambda: LisLegA(self.__bd))
        bll.grid(row=4, column=0)
        bli = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Listar inasistencias", command=lambda: LisInas(self.__bd))
        bli.grid(row=4, column=1)
        blc = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Listar curso", command=lambda: LisRegXCurso(self.__bd))
        blc.grid(row=5, column=0)
        blc = Button(self.__pp, height=heigth, width=width, relief="raised", borderwidth=borde, background=colorboton,
                     fg=colorletra, font=fuente, text="Salir", command=self.salir)
        blc.grid(row=5, column=1)
        self.__pp.mainloop()

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Desea salir? Perdera los datos no guardados."):
            self.__pp.destroy()

    def CargaBD(self):
        if self.__bd.leerArchivo():
            self.__abierto = True
            messagebox.showinfo("Exito", "Base de datos cargada con exito")
        else:
            messagebox.showerror("Error", "No se ha encontrado BD.txt")

    def Backup(self):
        if self.__abierto:
            self.__bd.escribirArchivo()
            messagebox.showinfo("Exito", "Backup realizado con exito")
        else:
            messagebox.showwarning("Advertencia", "No ha iniciado la sesion de trabajo.")
