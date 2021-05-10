
import csv,os

from claseCamion import Camion

from claseManejadorCamion import ManejadorCamion

class Cosecha:
    __lista = []

    def __init__(self):
        self.__lista = []
        self.inicializarLista()

    def inicializarLista(self):
        for i in range(45):
            self.__lista.append([])
            for j in range(20):
                self.__lista[i].append(0)

    def leerArchivo(self,unManejador):
        aux = ManejadorCamion()
        if type(aux) == type(unManejador):
            os.system ('cls')
            archivo = open('cosecha.csv')
            reader = csv.reader (archivo, delimiter= ';')
            i=0
            for fila in reader:
                for columna in range (20):
                    peso = float(fila[columna])
                    self.agregaCosecha(peso,i,columna,unManejador)
                i+=1
            archivo.close()

    def agregaCosecha(self, peso,fila,columna,unManejador): #Previamente se verificó unManejador
        if type(peso) == float:
            if type(fila) == int:
                if type(columna) == int:
                    aux = ManejadorCamion()
                    if type(aux) == type(unManejador):
                        if self.verificaPeso(columna+1,peso,unManejador):
                            kilos = self.calculaPeso(columna+1,peso,unManejador)
                            self.__lista[fila][columna] += kilos

    def verificaPeso(self,idCamion,peso, unManejador): #Previamente se verificó unManejador
        if type(idCamion) == int:
            if type(peso) == float:
                aux = ManejadorCamion()
                if type(aux) == type(unManejador):
                    unCamion = Camion()
                    listaCamiones = unManejador.getListaCamiones()
                    for unCamion in listaCamiones:
                        if unCamion.getIdCamion() == idCamion:
                            tara = unCamion.getTara()
                            if peso >= tara:
                                retorno=True
                            else:
                                retorno=False
                            return retorno

    def calculaPeso(self,idCamion,peso,unManejador):
        if type(idCamion) == int:
            if type(peso) == float:
                aux = ManejadorCamion()
                if type(aux) == type(unManejador):
                    unCamion = Camion()
                    listaCamiones = unManejador.getListaCamiones()
                    for unCamion in listaCamiones:
                        if unCamion.getIdCamion() == idCamion:
                            tara = unCamion.getTara()
                            kilos = peso - tara
                    return kilos
    
    def calculoTotal(self,idCamion,unaCosecha):
        if type(idCamion) == int:
            aux=Cosecha()
            if type(aux) == type(unaCosecha):
                total=0
                listaCosecha = unaCosecha.getListaCosecha()
                for i in range(len(listaCosecha)):
                        total+=listaCosecha[i][idCamion]
                return total

    def listadoDia(self,dia,unManejador,unaCosecha):
        if type(dia) == int:
            aux=ManejadorCamion()
            if type(aux) == type(unManejador):
                aux=Cosecha()
                if type(aux) == type(unaCosecha):
                    print ('PATENTE\t\tConductor\tKilos\n')
                    listaCamiones = unManejador.getListaCamiones()
                    unCamion = Camion()
                    for unCamion in listaCamiones:
                        patente = unCamion.getPatente()
                        conductor = unCamion.getConductor()
                        idCamion = unCamion.getIdCamion()
                        kilos = self.calculoTotal(idCamion-1,unaCosecha)
                        print (f'{patente}\t\t{conductor}\t\t{kilos}')

    def getListaCosecha(self):
        return self.__lista

    def __str__(self):
        return f'{self.__lista}'