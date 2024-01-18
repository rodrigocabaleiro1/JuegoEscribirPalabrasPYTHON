from principal import *
from configuracion import *

import random
import math
import time

# Se encarga de actualizar la pantalla, mueve las palabras y las hace aparecer
#en pantalla. Ademas borra las palabras que se escapan de la pantalla.
# La cantidad de paises y su velocidad de movimiento varian segun el
#tiempo y la dificultad seleccionada.
def actualizar(paisesEnPantalla,posiciones,listaPaises,dificultad,cantidad_paises,segundos,color):
    segundos=int(segundos)
    coloresAgregar=()
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)
    coloresAgregar=(color1,color2,color3)
    if (dificultad=="f"):
        confirmar=random.randint(1,3)
    elif(dificultad=="m"):
        confirmar=random.randint(1,2)
    else:
        confirmar=1
    if(confirmar==1):
        if (len(paisesEnPantalla) < cantidad_paises):
            paisAgregar = nuevoPais(listaPaises)
            if (paisAgregar not in paisesEnPantalla):
                paisesEnPantalla.append(paisAgregar)
                color.append(coloresAgregar)
                if (len(paisesEnPantalla) < 1):
                    posiciones.append(0)
                    posiciones.append(posicionVertical(posiciones))
                else:
                    xRandom=random.randint(0,250)
                    posicionY = posicionVertical(posiciones)
                    posiciones.append(xRandom)
                    posiciones.append(posicionY)

    #Velocidades y codiciones segun el tiempo
    for pais in range(len(paisesEnPantalla)):
        if(dificultad=="f"):
            posiciones [pais*2] += 20
        elif(dificultad=="m"):
            if (segundos>=30):
                posiciones [pais*2] += 20
            elif(segundos<30):
                posiciones [pais*2] += 40
        elif(dificultad=="d"):
            if(segundos>=30):
                posiciones [pais*2] += 20
            elif(segundos<30 and segundos>=10):
                posiciones [pais*2] += 40
            elif(segundos<10):
                posiciones [pais*2] += 60
    eliminar(paisesEnPantalla,posiciones,color)
    pass

"""def estaCerca(elem, lista):
    pass"""

#selecciona un pais aleatorio de la lista de paises
def nuevoPais(paises):
    paisSeleccionado = paises[random.randrange(len(paises))]
    return paisSeleccionado

# Elimina el pais que ingresamos por teclado de la lista de paises en pantalla y sus posiciones.
def quitar(candidata, paisesEnPantalla, posiciones,color):
    for i in range(len(paisesEnPantalla)):
        if(candidata.upper()==paisesEnPantalla[i]):
            paisesEnPantalla.pop(i)
            color.pop(i)
            posiciones.pop(i*2+1)
            posiciones.pop(i*2)
            return()

# Comprueba si la palabra ingresada es uno los paises en pantalla y si existe
# en la lista de paises
def esValida(candidata, listaPaises,paisesEnPantalla):
    if (candidata.upper() in listaPaises) and (candidata.upper()
    in paisesEnPantalla):
        return True
    else:
        return False

#Devuelve el puntaje obtenido con una palabra
def Puntos(candidata):
    puntaje = 0
    for caracter in candidata:
        if(detectarVocales(caracter) == True):
            puntaje = puntaje + 1
        elif(detectarConsonantesSimples(caracter) == True):
            puntaje = puntaje + 2
        elif(detectarConsonantesDificil(caracter) == True):
            puntaje = puntaje + 5

    return puntaje

#Comprueba si la palabra es valida y en funcion de eso borra la palabra en pantalla ingresada y devuelve el puntaje obtenido.
def procesar(candidata, listaPaises, paisesEnPantalla,posiciones,color):
    if(esValida(candidata, listaPaises, paisesEnPantalla) == True):
        puntaje = Puntos(candidata)
        quitar(candidata, paisesEnPantalla, posiciones,color)
        return puntaje
    else: return 0


#Funciones agregadas

def detectarVocales(caracter):
    if (caracter in "aeiou"):
        return True
    else:
        return False

def detectarConsonantesDificil(caracter):
    if (caracter in "jkqwxyz"):
        return True
    else:
        return False

def detectarConsonantesSimples(caracter):
    if(detectarVocales(caracter)== False) and (detectarConsonantesDificil(caracter) == False):
        return True
    else:
        return False


# Se encarga de asignar las posiciones en el eje Y de las palabras.
def posicionVertical (posiciones):
    if(250 not in posiciones):
        return 250

    posicionesY = []
    for posicion in range (0, len (posiciones), 2):
        posicionesY.append(posiciones[posicion + 1])
    #print(posicionesY)

    if(250 in posicionesY):
        over250 = 0
        sub250 = 0

        for posicion in range (len(posicionesY)):
            if(posicionesY[posicion] > 250):
                over250 += 1
            else:
                sub250 += 1

        yrandom = random.randint(1,7)
        for posicion in range (len(posicionesY)):
            if(over250 >= sub250):
                if((posicionesY [posicion] - yrandom * 25) not in posicionesY) and ((posicionesY[posicion] - yrandom * 25) > 0):
                    return posicionesY[posicion] - yrandom * 25
            else:
                if((posicionesY[posicion] + yrandom * 25) not in posicionesY) and ((posicionesY[posicion] + yrandom * 25) < 500):
                    return posicionesY[posicion] + yrandom * 25


# Se encarga de identificar los paises que se salen de la pantalla y los elimina
def eliminar(paisesEnPantalla,posiciones,color):
    for pais in range(len(paisesEnPantalla)):
        if(posiciones[pais*2] > ANCHO):
                paisesEnPantalla.pop(pais)
                color.pop(pais)
                posiciones.pop(pais*2+1)
                posiciones.pop(pais*2)
                return()
    pass
