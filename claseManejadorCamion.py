
import csv,os

from claseCamion import Camion


class ManejadorCamion:
    __lista = []
    
    def __init__(self):
        self.__lista = []


    def agregaCamion(self, unCamion):
        aux = Camion()
        if type(aux) == type(unCamion):
            self.__lista.append(unCamion)

    def leerArchivo(self):
        os.system ('cls')
        archivo = open('listaCamiones.csv')
        reader = csv.reader (archivo, delimiter= ';')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear bandera'''
                bandera = False
            else:
                idCamion = int(fila[0])
                nombreConductor = fila[1]
                patente = fila[2]
                marca = fila [3]
                tara = float(fila [4])
                unCamion = Camion(idCamion, nombreConductor, patente, marca, tara)
                self.agregaCamion(unCamion)
        archivo.close()

    def getListaCamiones(self):
        return self.__lista

    def __str__(self):
        s=''
        unCamion = Camion()
        for unCamion in self.__lista:
            s+=unCamion.__str__() + '\n\n'
        return s