from tkinter import *
from tkinter import ttk, messagebox

from MostrarTabla import *


class LisRegXCurso:
    def __init__(self, bd):
        if bd.isEmptyAlumno():
            messagebox.showwarning("Advertencia", "No hay alumnos cargados en la BD.")
        else:
            pantalla = Toplevel()
            pantalla.grab_set()
            pantalla.resizable(0, 0)
            w = 280
            h = 80
            ws = pantalla.winfo_screenwidth()
            hs = pantalla.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            colorboton = "#000000"
            colorletra = "#d35400"
            fuente = "Helvetica 9"
            borde = 5
            pantalla.geometry('%dx%d+%d+%d' % (w, h, x, y))
            pantalla.title('Listar curso')
            lseleccione = Label(pantalla, text="Seleccione el curso")
            lseleccione.grid(row=0, column=0, padx=10, pady=10)
            combo = ttk.Combobox(pantalla, state='readonly')
            valores = bd.listaCursos()
            combo["values"] = valores
            combo.set(valores[0])
            combo.grid(row=0, column=1, columnspan=2)
            bseleccione = Button(pantalla, relief="raised", borderwidth=borde, fg=colorletra,
                                 background=colorboton, font=fuente, text="Ver listado",
                                 command=lambda: MostrarTabla(bd, int(combo.get())))
            bseleccione.grid(row=1, column=1)
            pantalla.mainloop()
