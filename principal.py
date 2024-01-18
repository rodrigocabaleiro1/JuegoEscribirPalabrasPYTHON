#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
import csv
from configuracion import *
from funcionesVACIAS import *
from extras import *
#Menu
def pantalla_inicio():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Fast Fast...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    fondo = pygame.image.load("fondo.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    logo=pygame.image.load("logoo.png")
    logo = pygame.transform.scale(logo, (644, 208))

    screen.blit(fondo, (0, 0))      #muestra en pantalla la imagen de fondo
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)

    screen.blit(logo,(ANCHO//2 - logo.get_width()//2,50))

    texto_dificultad = defaultFont.render("Seleccionar dificultad",1,COLOR_FONDO)
    screen.blit(texto_dificultad, (ANCHO // 2 - texto_dificultad.get_width() // 2, ALTO // 2))

    texto_facil = defaultFont.render("Presiona 1 para Fácil", 1, COLOR_FONDO)
    screen.blit(texto_facil, (ANCHO // 2 - texto_facil.get_width() // 2, ALTO // 2 + 50))

    texto_medio = defaultFont.render("Presiona 2 para Medio", 1, COLOR_FONDO)
    screen.blit(texto_medio, (ANCHO // 2 - texto_medio.get_width() // 2, ALTO // 2 + 100))

    texto_dificil = defaultFont.render("Presiona 3 para Difícil", 1, COLOR_FONDO)
    screen.blit(texto_dificil, (ANCHO // 2 - texto_dificil.get_width() // 2, ALTO // 2 + 150))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return ("s",0)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return ("s",0)
                elif evento.key == pygame.K_1:
                    pygame.quit()
                    return ("f",3)
                elif evento.key == pygame.K_2:
                    pygame.quit()
                    return ("m",4)
                elif evento.key == pygame.K_3:
                    pygame.quit()
                    return ("d",5)
        pygame.display.flip()
#Ingresar nombre
def ingresar_nombre(puntos,dificultad):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Fast Fast...")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    clock=pygame.time.Clock()
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MED)
    texto=""
    salir=""
    input_active = True
    texto_nombre=defaultFontGrande.render("Ingresa tu nombre:", 1, COLOR_TEXTO)
    screen.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, 20))
    while input_active==True:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                texto = ""
            elif evento.type == pygame.KEYDOWN and input_active:
                if evento.key == pygame.K_RETURN:
                    if(dificultad=="f"):
                        with open('puntosfacil.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')
                    elif(dificultad=="m"):
                        with open('puntosmedio.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')
                    elif(dificultad=="d"):
                        with open('puntosdificil.txt', 'a') as f:
                            f.write(texto+","+str(puntos))
                            f.write('\n')

                    pygame.quit()
                    salir=pantalla_final(puntos,dificultad)

                elif evento.key == pygame.K_BACKSPACE:
                    texto =  texto[:-1]
                else:
                    texto += evento.unicode
            if(salir!="s"):
                screen.fill(0)
                text_surf = defaultFont.render(texto, True, (255, 0, 0))
                screen.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, 20))
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                pygame.display.flip()
            else:
                input_active = False
#Pantalla final
def pantalla_final(puntos,dificultad):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.display.set_caption("Fast Fast...")
    screen = pygame.display.set_mode((ANCHO, ALTO))
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MED)
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    texto_puntos=defaultFontGrande.render("Hiciste "+str(puntos)+" puntos", 1, COLOR_LETRAS)
    screen.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() // 2, 20))
    ranking=""
    y_pos1=120
    y_pos2=120
    cont=0
    pygame.draw.line(screen, (200, 200, 200), (0, 100), (ANCHO, 100), 5)
    if(dificultad=="f"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (facil)", 1, COLOR_TEXTO)
        with open("puntosfacil.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    elif(dificultad=="m"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (medio)", 1, COLOR_TEXTO)
        with open("puntosmedio.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    elif(dificultad=="d"):
        texto_ranking = defaultFont.render("Mejores puntuaciones (dificil)", 1, COLOR_TEXTO)
        with open("puntosdificil.txt") as file:
            csv_reader = csv.reader(file)
            sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)
    screen.blit(texto_ranking, (ANCHO // 2 - texto_ranking.get_width() // 2, 120))
    for nom, pun in sorted_list:
        cont=cont+1
        ranking=("{0} - {1}".format(nom, pun))
        listapuntos=defaultFont.render(ranking, 1, COLOR_TEXTO)
        if(cont<=5):
            y_pos1=y_pos1+ESPACIO
            screen.blit(listapuntos,(ANCHO // 2 - texto_ranking.get_width() // 2, y_pos1))
        elif(cont>5 and cont <=10):
            y_pos2=y_pos2+ESPACIO
            screen.blit(listapuntos,(ANCHO // 2 + 65, y_pos2))
        else:
            break
    texto_menu=defaultFont.render("1 - Menu",1,COLOR_TEXTO)
    screen.blit(texto_menu, (10, 550))
    texto_salir=defaultFont.render("esc - Salir",1,COLOR_TEXTO)
    screen.blit(texto_salir, (600, 550))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return("s")
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return("s")
                elif evento.key == pygame.K_1:
                    pygame.quit()
                    main()
        pygame.display.flip()

#Funcion principal
def main():
        eleccion = ""
        if(eleccion == ""):
            eleccion = pantalla_inicio()
        dificultad = eleccion[0]
        cantidad_paises = eleccion[1]
        if (dificultad == "s"):
            pygame.quit()
            return
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Fast Fast...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        fondo2 = pygame.image.load("fondo3.png")
        fondo2 = pygame.transform.scale(fondo2, (ANCHO, ALTO))
        screen.blit(fondo2, (0, 0))
        pygame.mixer.init()
        acierto=pygame.mixer.Sound('acierto.mp3')
        fallo=pygame.mixer.Sound('fallo.mp3')
        tiempo=pygame.mixer.Sound('vida.mp3')
        musicaDeFondo = pygame.mixer.Sound('musica.mp3')
        musicaDeFondo.play(-1)
        musicaDeFondo.set_volume(0.25)
        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial


        cont=0
        puntos = 0
        candidata = ""
        listaPaises=[]
        posiciones = []
        paisesEnPantalla=[]
        color=[]
        archivo= open("paises.txt","r")
        for linea in archivo.readlines():
            listaPaises.append(linea[0:-1])

        dibujar(screen, candidata, paisesEnPantalla, posiciones, puntos,segundos,color)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        calculo=procesar(candidata, listaPaises, paisesEnPantalla,posiciones,color)
                        if (calculo>0):
                            acierto.play()
                        else:
                            fallo.play()
                        puntos += calculo
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
            if(int(segundos)==15 and cont==0):
                cont=cont+1
                tiempo.play(-1)
                tiempo.set_volume(0.25)
            #Limpiar pantalla anterior
            screen.blit(fondo2, (0, 0))

            #Dibujar de nuevo todo
            dibujar(screen, candidata, paisesEnPantalla, posiciones, puntos, segundos,color )

            pygame.display.flip()

            actualizar(paisesEnPantalla, posiciones, listaPaises,dificultad,cantidad_paises,segundos,color)

        pygame.quit()
        ingresar_nombre(puntos,dificultad)

#Programa Pirncipal ejecuta Main
if __name__ == "__main__":
    main()
