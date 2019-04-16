class Alumno:
    def __init__(self, nroRegistro, nombre, DNI, direccion, telefono, email, fechaNacimiento, curso, fechaAlta,
                 fechaBaja, concepto, inasistencias, materias, usuario, contrasena):
        self.__nroRegistro = nroRegistro
        self.__nombre = nombre
        self.__DNI = DNI
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fechaNacimiento = fechaNacimiento
        self.__curso = curso
        self.__fechaAlta = fechaAlta
        self.__fechaBaja = fechaBaja
        self.__concepto = concepto
        self.__inasistencias = inasistencias
        self.__materias = materias
        self.__usuario = usuario
        self.__contrasena = contrasena

    def getNroRegistro(self):
        return self.__nroRegistro

    def getNombre(self):
        return self.__nombre

    def getDNI(self):
        return self.__DNI

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    def getEmail(self):
        return self.__email

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def getCurso(self):
        return self.__curso

    def getFechaAlta(self):
        return self.__fechaAlta

    def getFechaBaja(self):
        return self.__fechaBaja

    def getConcepto(self):
        return self.__concepto

    def getInasistencias(self):
        return self.__inasistencias

    def getMaterias(self):
        return self.__materias

    def getUsuario(self):
        return self.__usuario

    def getContrasena(self):
        return self.__contrasena
