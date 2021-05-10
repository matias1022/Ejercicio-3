
class Camion:
    __identificador = 1
    __nombreConductor = None
    __patente = None
    __marca = None
    __tara = 0

    def __init__ (self, identificador = 1, nombreConductor = '', patente = '', marca = '', tara = 0):
        if self.verificaDatos(identificador,nombreConductor,patente,marca,tara):
            self.__identificador = identificador
            self.__nombreConductor = nombreConductor
            self.__patente = patente
            self.__marca = marca
            self.__tara = tara
        else:
            self.__identificador = 1
            self.__nombreConductor = ''
            self.__patente = ''
            self.__marca = ''
            self.__tara = 0

    def verificaDatos(self,identificador,nombreConductor,patente,marca,tara):
        if type(identificador) == int:
            if 1<=identificador<=20:
                if type(nombreConductor) == str:
                    if type(patente) == str:
                        if type(marca) == str:
                            if type(tara) == float:
                                retorno=True
                            else:
                                retorno=False
                        else:
                            retorno=False
                    else:
                        retorno=False
                else:
                    retorno=False
            else:
                retorno=False
        else:
            retorno=False
        return retorno


    def getIdCamion(self):
        return self.__identificador

    def getTara(self):
        return self.__tara

    def getPatente(self):
        return self.__patente

    def getConductor(self):
        return self.__nombreConductor

    def __str__(self):
        return f'''Identificador: {self.__identificador}.
Nombre Conductor: {self.__nombreConductor}.
Patente: {self.__patente}.
Marca: {self.__marca}.
Tara: {self.__tara} Kg.'''