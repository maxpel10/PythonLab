class Materia:
    def __init__(self, codigoMateria, codigoAlumno, nombre, notas):
        self.__codigoMateria = codigoMateria
        self.__codigoAlumno = codigoAlumno
        self.__nombre = nombre
        self.__notas = notas

    def getCodigoMateria(self):
        return self.__codigoMateria

    def getCodigoAlumno(self):
        return self.__codigoAlumno

    def getNombre(self):
        return self.__nombre

    def getNotas(self):
        return self.__notas
