import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")

    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def PasarACadena(lista):
    cadena="".join(lista)
    return cadena


def dibujar(screen, candidata, palabraActual, oculta, puntos, segundos,puntosAnteriores,record):

    imagen=pygame.image.load("Wallpaper Matrix.jpg")                        #carga la imagen de fondo
    screen.blit(imagen,(0,0))                                               #Pone la imagen

    defaultFontChica= pygame.font.Font( pygame.font.get_default_font(), 17)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)
    ##screen.blit(defaultFont.render(palabraActual, 1, COLOR_TEXTO), (500, 100))             #Para testear

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(candidata, 1, COLOR_TEXTO), (190, 570))

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (640, 10))
    #muestra los puntos que sumo con la palabra anterior
    screen.blit(defaultFontChica.render("Puntos sumados: "+ str(puntosAnteriores),1,(240,248,255)), (625, 40))

    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la palabra con *
    screen.blit(defaultFontGrande.render(PasarACadena(oculta), 1, COLOR_LETRAS), (100,ALTO-400))
    #muestra su longitud
    screen.blit(defaultFontGrande.render(str(len(palabraActual)), 1, (200,20,10)), (ANCHO-400,ALTO-500))
    #muestra todo el tiempo el mejor record
    screen.blit(defaultFontChica.render("Mejor record: "+str(record),1,(255,255,255)),(ANCHO-170,ALTO-100))
    #cuando termine el tiempo muestra todo lo siguiente
    if segundos<1:
        screen.fill(COLOR_FONDO)
        screen.blit(defaultFontGrande.render("GAME OVER", 1, COLOR_LETRAS), (160,ALTO-400))

        #si supero el record maximo hace lo siguiente
        if int(record) < puntos:
            screen.blit(defaultFont.render(("Superastes el record maximo! Tu record es: "+str(puntos)), 1, COLOR_TEXTO), (100,ALTO-200))
        else:

            screen.blit(defaultFont.render(("Puntaje total: "+str(puntos)), 1, COLOR_TEXTO), (300,ALTO-200))







