
import os

from claseCamion import Camion

from claseCosecha import Cosecha

from claseManejadorCamion import ManejadorCamion


class MenuOpciones:
    # Constantes
    CONSULTAR = 1
    LISTAR = 2
    SALIR = 0

    # Atributos
    __opc=None

    # Constructor
    def __init__(self,opc=0):
        self.__opc=opc

    # Métodos
    def menuOpciones (self, unManejador, unaCosecha):
        aux = ManejadorCamion()
        if type(aux) == type(unManejador):
            aux = Cosecha()
            if type(aux) == type(unaCosecha):
                continuar = True
                while continuar:
                    os.system ('cls')
                    print (f'''          Menú de opciones:
{self.CONSULTAR}) Consultar Cantidad Total de Kilos descargados de un camión.
{self.LISTAR}) Listado de camiones con respecto a un día.
{self.SALIR}) Salir.
''')
                    opc = input ('Ingrese una opción: ')
                    if opc.isdigit():
                        self.__opc = int (opc)
                        os.system ('cls')
                        if self.__opc == self.CONSULTAR:
                            print ('            CANTIDAD TOTAL DE KILOS DESCARGADOS.')
                            idCamion = input('Ingrese el identificador del camión: ')
                            if idCamion.isdigit():
                                idCamion = int(idCamion)
                                if 1<=idCamion<=20:
                                    total = unaCosecha.calculoTotal(idCamion-1, unaCosecha)
                                    print(f'El total de kilos descargados del Camión {idCamion} es: {total} kg.')
                                else:
                                    print('El identificador del camión es incorrecto.')
                        elif self.__opc == self.LISTAR:
                            print ('            LISTADO DE CAMIONES.')
                            dia = input ('Ingrese un día: ')
                            if dia.isdigit():
                                dia = int (dia)
                                if 1<=dia<=45:
                                    unaCosecha.listadoDia(dia-1,unManejador,unaCosecha)
                                else:
                                    print ('El día ingresado es incorrecto.')
                            else:
                                print ('Número de millas INCORRECTO.')
                        elif self.__opc == self.SALIR:
                            continuar = False
                        else:
                            print ('Opción no válida.')
                        input ('Presiona ENTER para continuar...')
                    else:
                        print ('Opción no válida.')
                        input ('Presiona ENTER para continuar...')
                print ('¡Nos vemos!')