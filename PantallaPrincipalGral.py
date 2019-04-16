from LisInas import *
from LisLegA import *
from LisRegXCurso import *
from LisTAlu import *
from LisTMat import *
from tkinter import *
from tkinter import messagebox


class PantallaPrincipalGral:
    def __init__(self, login, bd):
        login.destroy()
        self.__bd = bd
        self.__pp = Tk()
        self.__pp.resizable(0, 0)
        w = 432
        h = 168
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
        self.__pp.title('Menú principal')
        self.__pp.protocol("WM_DELETE_WINDOW", self.salir)
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
        if messagebox.askokcancel("Salir", "¿Desea salir?"):
            self.__pp.destroy()
