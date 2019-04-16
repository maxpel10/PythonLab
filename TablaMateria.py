class TablaMateria:
    def __init__(self, tabla):
        self.__tabla = tabla

    def getTabla(self):
        return self.__tabla

    def isEmpty(self):
        return self.__tabla == []

    def setTabla(self, tabla):
        self.__tabla = tabla
