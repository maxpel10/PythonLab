from Materia import *
from TablaAlumno import *
from TablaMateria import *
from Alumno import *
from functools import reduce
import time


def ordenacion(x, y):
    if len(x) == 0:
        x.append(y)
    else:
        for indice, valor in enumerate(x):
            if y[0] < valor[0]:
                x.insert(indice, y)
                break
        else:
            x.append(y)
    return x


class BD_Escuela:
    def __init__(self):
        self.__cant_Usuarios = 1
        self.__acceso = {"P-Admin": "Ad1"}
        self.__nbreTablas = {"T_Alumnos": 0, "T_Materias": 1}
        self.__tablas = [TablaAlumno([]), TablaMateria([])]

    def setCant_Usuarios(self, cant_Usuarios):
        self.__cant_Usuarios = cant_Usuarios

    def getCant_Usuarios(self):
        return self.__cant_Usuarios

    def validarIngreso(self, user, password):
        try:
            userAdm = "P-" + user
            if self.__acceso[userAdm] == password:
                return 1
        except KeyError:
            userAlum = "A-" + user
            try:
                if self.__acceso[userAlum] == password:
                    return 2
            except KeyError:
                userDoc = "D-" + user
                try:
                    if self.__acceso[userDoc] == password:
                        return 3
                except KeyError:
                    return 4

    def leerArchivo(self):
        self.__cant_Usuarios = 0
        self.__acceso = {}
        self.__nbreTablas = {}
        self.__tablas = []
        try:
            archivo = open("BD.txt")
            lineas = archivo.readlines()
            self.__cant_Usuarios = int(lineas[1][22:-1])
            i = 4
            while lineas[i] != "-\n":
                self.__acceso[lineas[i][:-1]] = lineas[i + 1][:-1]
                i = i + 2
            i = i + 3
            while lineas[i] != "-\n":
                self.__nbreTablas[lineas[i][:-1]] = int(lineas[i + 1][:-1])
                i = i + 2
            tablaAlumnos = []
            i = i + 5
            while lineas[i] != "-\n":
                fechaNacimiento = lineas[i + 6][:-1].split(" ")
                fechaAlta = lineas[i + 8][:-1].split(" ")
                fechaBaja = lineas[i + 9][:-1].split(" ")
                fechaNacimiento = (int(fechaNacimiento[0]), int(fechaNacimiento[1]), int(fechaNacimiento[2]))
                fechaAlta = (int(fechaAlta[0]), int(fechaAlta[1]), int(fechaAlta[2]))
                fechaBaja = (int(fechaBaja[0]), int(fechaBaja[1]), int(fechaBaja[2]))
                alumno = (int(lineas[i][:-1]), lineas[i + 1][:-1], int(lineas[i + 2][:-1]), lineas[i + 3][:-1],
                          int(lineas[i + 4][:-1]), lineas[i + 5][:-1], fechaNacimiento, int(lineas[i + 7][:-1]),
                          fechaAlta, fechaBaja, lineas[i + 10][:-1], int(lineas[i + 11][:-1]), lineas[i + 12][:-1],
                          lineas[i + 13][:-1])
                tablaAlumnos.append(alumno)
                i = i + 15
            self.__tablas.append(TablaAlumno(tablaAlumnos))
            tablaMaterias = []
            i = i + 3
            while lineas[i] != "-\n":
                notas = lineas[i + 3][:-1].split(" ")
                notas = (int(notas[0]), int(notas[1]), int(notas[2]))
                materia = (int(lineas[i][:-1]), int(lineas[i + 1][:-1]), lineas[i + 2][:-1], notas)
                tablaMaterias.append(materia)
                i = i + 5
            self.__tablas.append(TablaMateria(tablaMaterias))
            archivo.close()
            return True
        except FileNotFoundError:
            return False

    def escribirArchivo(self):
        archivo = open("BD.txt", "w")
        l = ["Informacion BD\n", "Cantidad de usuarios: " + str(self.__cant_Usuarios) + "\n", "\n", "Acceso:\n"]
        claves = self.__acceso.keys()
        for i in claves:
            l.append(i + "\n")
            l.append(self.__acceso[i] + "\n")
        l.append("-\n")
        l.append("\n")
        l.append("Nombre Tablas:\n")
        claves = self.__nbreTablas.keys()
        for i in claves:
            l.append(i + "\n")
            l.append(str(self.__nbreTablas[i]) + "\n")
        l.append("-\n")
        l.append("\n")
        l.append("Tablas\n")
        l.append("\n")
        l.append("Alumnos:\n")
        for i in self.__tablas[0].getTabla():
            l.append(str(i[0]) + "\n")
            l.append(i[1] + "\n")
            l.append(str(i[2]) + "\n")
            l.append(i[3] + "\n")
            l.append(str(i[4]) + "\n")
            l.append(i[5] + "\n")
            l.append(str(i[6][0]) + " " + str(i[6][1]) + " " + str(i[6][2]) + "\n")
            l.append(str(i[7]) + "\n")
            l.append(str(i[8][0]) + " " + str(i[8][1]) + " " + str(i[8][2]) + "\n")
            l.append(str(i[9][0]) + " " + str(i[9][1]) + " " + str(i[9][2]) + "\n")
            l.append(i[10] + "\n")
            l.append(str(i[11]) + "\n")
            l.append(str(i[12]) + "\n")
            l.append(str(i[13]) + "\n")
            l.append("\n")
        l.append("-\n")
        l.append("\n")
        l.append("Materias:\n")
        for i in self.__tablas[1].getTabla():
            l.append(str(i[0]) + "\n")
            l.append(str(i[1]) + "\n")
            l.append(i[2] + "\n")
            l.append(str(i[3][0]) + " " + str(i[3][1]) + " " + str(i[3][2]) + "\n")
            l.append("\n")
        l.append("-\n")
        archivo.writelines(l)
        archivo.close()

    def existeUsuario(self, user):
        claves = self.__acceso.keys()
        if "P-" + user in claves or "A-" + user in claves or "D-" + user in claves:
            return True
        else:
            return False

    def existeDNI(self, dni):
        for i in self.__tablas[0].getTabla():
            if dni == i[2]:
                return True
        return False

    def existeNombreMateria(self, nombre):
        for i in self.__tablas[1].getTabla():
            if nombre == i[2]:
                return True
        return False

    def altaUsuario(self, user, password):
        self.__acceso[user] = password
        self.__cant_Usuarios = self.__cant_Usuarios + 1

    def getListaUsuarios(self):
        claves = self.__acceso.keys()
        listaClaves = []
        for i in claves:
            listaClaves.append(i)
        return listaClaves
    # Hago esto porque sino me devuelve una dict_keys  y yo necesito una lista

    def bajaUsuario(self, user):
        del self.__acceso[user]
        self.__cant_Usuarios = self.__cant_Usuarios - 1

    def getAlumno(self, cod_alu):
        tablaAlumnos = self.__tablas[0].getTabla()
        tablaMaterias = self.__tablas[1].getTabla()
        alumnoRetorno = False
        listaMaterias = []
        for i in tablaAlumnos:
            if i[0] == cod_alu:
                for j in tablaMaterias:
                    if j[1] == cod_alu:
                        listaMaterias.append(Materia(j[0], j[1], j[2], j[3]))
                alumnoRetorno = Alumno(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11],
                                       listaMaterias, i[12], i[13])
                break
        return alumnoRetorno

    def estaDadoDeBaja(self, cod_alu):
        tablaAlumnos = self.__tablas[0].getTabla()
        retorno = False
        for i in tablaAlumnos:
            if i[0] == cod_alu and i[9] != (0, 0, 0):
                retorno = True
                break
        return retorno

    def isEmptyAlumno(self):
        return self.__tablas[0].isEmpty()

    def isEmptyMateria(self):
        return self.__tablas[1].isEmpty()

    def getMaximoNroRegistro(self):
        max = 1000
        for i in self.__tablas[0].getTabla():
            if i[0] > max:
                max = i[0]
        return max

    def getMaximoCodigoMateria(self):
        max = 0
        for i in self.__tablas[1].getTabla():
            if(i[0]) > max:
                max = i[0]
        return max

    def altaAlumno(self, alumno):
        a = (alumno.getNroRegistro(), alumno.getNombre(), alumno.getDNI(), alumno.getDireccion(), alumno.getTelefono(),
             alumno.getEmail(), alumno.getFechaNacimiento(), alumno.getCurso(), alumno.getFechaAlta(),
             alumno.getFechaBaja(), alumno.getConcepto(), alumno.getInasistencias(), alumno.getUsuario(),
             alumno.getContrasena())
        self.__tablas[0].getTabla().append(a)
        self.altaUsuario(alumno.getUsuario(), alumno.getContrasena())
        materias = [(1, alumno.getNroRegistro(), "Matematica", (0, 0, 0)),
                    (2, alumno.getNroRegistro(), "Lengua", (0, 0, 0)),
                    (3, alumno.getNroRegistro(), "Fisica", (0, 0, 0)),
                    (4, alumno.getNroRegistro(), "Quimica", (0, 0, 0)),
                    (5, alumno.getNroRegistro(), "Biologia", (0, 0, 0)),
                    (6, alumno.getNroRegistro(), "Etica", (0, 0, 0)),
                    (7, alumno.getNroRegistro(), "Historia", (0, 0, 0)),
                    (8, alumno.getNroRegistro(), "Geografia", (0, 0, 0)),
                    (9, alumno.getNroRegistro(), "Computacion", (0, 0, 0))]
        tablaMaterias = self.__tablas[1].getTabla()
        for i in materias:
            tablaMaterias.append(i)

    def altaMateria(self, materia):
        tablaAlumnos = self.__tablas[0].getTabla()
        tablaMaterias = self.__tablas[1].getTabla()
        for i in tablaAlumnos:
            m = (materia.getCodigoMateria(), i[0], materia.getNombre(), materia.getNotas())
            tablaMaterias.append(m)

    def bajaAlumno(self, nroRegistro):
        tablaAlumnos = self.__tablas[0].getTabla()
        a = 0
        alumno = ""
        for i in range(0, len(tablaAlumnos)):
            if nroRegistro == tablaAlumnos[i][0]:
                alumno = tablaAlumnos[i]
                a = i
                break
        nuevaFechaBaja = (int(time.strftime("%d")), int(time.strftime("%m")), int(time.strftime("%y"))+2000)
        nuevoAlumno = (alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5], alumno[6],
                       alumno[7], alumno[8], nuevaFechaBaja, alumno[10], alumno[11], alumno[12], alumno[13])
        tablaAlumnos[a] = nuevoAlumno
        self.bajaUsuario(tablaAlumnos[a][12])

    def modificarAlumno(self, am, usuarioAntiguo):
        tablaAlumnos = self.__tablas[0].getTabla()
        a = 0
        for i in range(0, len(tablaAlumnos)):
            if am.getNroRegistro() == tablaAlumnos[i][0]:
                a = i
                break
        alumno = (am.getNroRegistro(), am.getNombre(), am.getDNI(), am.getDireccion(), am.getTelefono(), am.getEmail(),
                  am.getFechaNacimiento(), am.getCurso(), am.getFechaAlta(), am.getFechaBaja(), am.getConcepto(),
                  am.getInasistencias(), am.getUsuario(), am.getContrasena())
        tablaAlumnos[a] = alumno
        if am.getFechaBaja() == (0, 0, 0):
            self.bajaUsuario(usuarioAntiguo)
            self.altaUsuario(am.getUsuario(), am.getContrasena())

    def modificarMateria(self, materia):
        tablaMaterias = self.__tablas[1].getTabla()
        a = 0
        for i in range(0, len(tablaMaterias)):
            if materia.getCodigoMateria() == tablaMaterias[i][0] and materia.getCodigoAlumno() == tablaMaterias[i][1]:
                a = i
                break
        materia = (materia.getCodigoMateria(), materia.getCodigoAlumno(), materia.getNombre(), materia.getNotas())
        tablaMaterias[a] = materia

    def getListaAlumnos(self):
        listaAlumnos = []
        for i in self.__tablas[0].getTabla():
            listaAlumnos.append(Alumno(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10],
                                       i[11], [], i[12], i[13]))
        return listaAlumnos

    def getListaMaterias(self):
        listaMaterias = []
        for i in self.__tablas[1].getTabla():
            listaMaterias.append(Materia(i[0], i[1], i[2], i[3]))
        return listaMaterias

    def getAlumnoDNI(self, dni):
        tablaAlumnos = self.__tablas[0].getTabla()
        alumnoRetorno = False
        for i in tablaAlumnos:
            if i[2] == dni:
                alumnoRetorno = Alumno(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], [],
                                       i[12], i[13])
                break
        return alumnoRetorno

    def getAReadmitir(self):
        return list(map(lambda x: [x[1], x[7], x[10]], filter(lambda x: x[11] > 15, self.__tablas[0].getTabla())))

    def getRegistroXCurso(self, curso):
        lista = map(lambda x: [x[1], x[2], x[0]], reduce(lambda x, y: x+[y] if y[7] == curso else x,
                    self.__tablas[0].getTabla(), []))
        return reduce(lambda x, y: ordenacion(x, y), lista, [])

    def listaCursos(self):
        tablaAlumnos = self.__tablas[0].getTabla()
        cursos = []
        for i in tablaAlumnos:
            if not str(i[7]) in cursos:
                cursos.append(str(i[7]))
        return sorted(cursos)
