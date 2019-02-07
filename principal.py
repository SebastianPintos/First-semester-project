#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()
        reloj=pygame.mixer.Sound("Clock.ogg")
        incorrecto=pygame.mixer.Sound("Incorrecto.ogg")
        acierto=pygame.mixer.Sound("Acierto.ogg")
        musicaDeFondo=pygame.mixer.Sound("Tema.ogg")
        pygame.mixer.Sound.play(musicaDeFondo)

        #Preparar la ventana
        gameDisplay=pygame.display.set_mode((ANCHO,ALTO))
        pygame.display.set_caption("Pasa palabra...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        defaultFont= pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)


        #tiempo total del juego
        puntajeTotal=0
        puntosAnteriores=0
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        f=open("records.txt","r")

        record=f.readline()

        puntos = 0
        candidata = ""
        listaFrases=[]
        listaPalabrasDiccionario=[]


        archivo= open("Matrix1999.srt","r")
        archivo2= open ("lemario.txt","r")
        #lectura del diccionario
        lectura2(archivo2, listaPalabrasDiccionario)

        #lectura del archivo. Cada linea es una frase
        lectura(archivo, listaFrases)

        #de cada frase elige la palabra mas larga
        listaPalabrasPeli=frasesToPalabras(listaFrases)

        #elige una al azar
        palabraActual=nuevaPalabra(listaPalabrasPeli)

        oculta=seleccionDeLetras(palabraActual)

        dibujar(screen, candidata, palabraActual, oculta, puntos,segundos,puntosAnteriores,record)
        screen.blit(defaultFont.render((palabraActual),1,COLOR_TEXTO),(10,60))


        while segundos > fps/1000:


            if segundos<13 and segundos>12.8:
                pygame.mixer.Sound.play(reloj)



        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 30

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


                    #Diferentes niveles automaticos segun el puntaje


                        if puntos<=100:
                            musica(candidata,oculta,palabraActual,incorrecto,acierto, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntos += procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntosAnteriores=procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntajeTotal=puntos
                            palabraActual=nuevaPalabra(listaPalabrasPeli)
                            oculta=seleccionDeLetras(palabraActual)
                            candidata = ""

                        elif  puntos>100 and puntos<200:


                            musica(candidata,oculta,palabraActual,incorrecto,acierto, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntos += procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntosAnteriores=procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntajeTotal=puntos
                            palabraActual=nuevaPalabra(listaPalabrasPeli)
                            oculta=seleccionDeLetras2(palabraActual)
                            candidata = ""

                        else:

                            musica(candidata,oculta,palabraActual,incorrecto,acierto, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntos += procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntosAnteriores=procesar(candidata, oculta, palabraActual, listaPalabrasPeli, listaPalabrasDiccionario)
                            puntajeTotal=puntos
                            palabraActual=nuevaPalabra(listaPalabrasPeli)
                            oculta=seleccionDeLetras3(palabraActual)
                            candidata = ""


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, palabraActual, oculta, puntos,segundos,puntosAnteriores,record)


            pygame.display.flip()
            f.close()

        #Guarda el puntaje hecho si es mejor que el maximo record.
        if str(puntajeTotal)>record:
            f.close()
            w=open("records.txt","w")
            w.write(str(puntos))
            w.close()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

