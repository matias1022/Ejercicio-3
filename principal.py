
import os

from claseCamion import Camion

from claseCosecha import Cosecha

from claseManejadorCamion import ManejadorCamion

from claseMenuOpciones import MenuOpciones

def test():
    unManejador = ManejadorCamion()
    Camion1 = Camion()
    unManejador.agregaCamion(Camion1)
    print ('Camiones test:')
    print (unManejador)
    input ('Presiona ENTER para continuar...')

if __name__ == '__main__':
    test()
    unManejador = ManejadorCamion()
    unaCosecha = Cosecha()
    unMenu = MenuOpciones()
    unManejador.leerArchivo()
    unaCosecha.leerArchivo(unManejador)
    idCamion = input('Ingrese el identificador del camión: ')
    if idCamion.isdigit():
        idCamion = int(idCamion)
        if 1<=idCamion<=20:
            dia = input ('Ingrese un día: ')
            if dia.isdigit():
                dia = int (dia)
                if 1<=dia<=45:
                    peso = input('Ingrese el peso de camión: ')
                    if peso.isdigit():
                        peso = float(peso)
                        unaCosecha.agregaCosecha(peso,dia-1,idCamion-1,unManejador)
                else:
                    print ('El día ingresado es incorrecto.')
        else:
            print('El identificador del camión es incorrecto.')
    input('Presione ENTER para continuar...')
    unMenu.menuOpciones(unManejador,unaCosecha)
    