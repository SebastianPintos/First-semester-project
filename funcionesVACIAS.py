from principal import *
from configuracion import *
# -*- coding: 850 -*-
# -*- coding: cp1252 -*-

import random
import math


def elegirLaMasLarga(listaPalabras):
    listaNueva=[]
    for elemento in listaPalabras:   #se recorre la lista
        if len(elemento)>=4:          #solo se toman las palabras de 4 o mas letras
            listaNueva.append(elemento) #Se agregan a la lista nueva
    return listaNueva      #devuelve la lista con las palabras de 4 o mas letras


def frasesToPalabras(listaFrases):
    listaNueva=[]
    cadena=""
    for elemento in listaFrases:         #se recorre por elemento la lista con las frases
        for letra in elemento:           #se recorre la letra de cada frase/elemento
            if letra!= " ":               # mientras no se encuentre un espacio, se concatena cada letra recorrida
                cadena=cadena+letra
            else:
                listaNueva.append(cadena)    #si se encuentra un espacio, se guarda lo que tenia hasta ese momento la cadena
                cadena=""                    #se "resetea" el valor de la cadena a vacio
        listaNueva.append(cadena)            #guarda la ultima palabra de cada frase, ya que al no haber un espacio no se podria separar como las demas
        cadena=""
    return elegirLaMasLarga(listaNueva)      #se devuelven las palabras de mas de 4 letras solamente

def esta(a,lista):
    for elemento in lista:
        if elemento==a:
            return True
    return False

def PasarACadena(lista):
    cadena="".join(lista)    #encontramos esta funcion en internet para pasar de forma mas facil una lista a cadena
    return cadena

def quitarCaracteresEspeciales(linea):
    cadena=""
    listaABC=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", " ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for letra in linea:
        if esta(letra,listaABC):         #si la primer letra de cada linea esta en el abecedario, se guarda en la cadena
            cadena=cadena+letra.lower()
        elif letra == "á" or letra=="Á":     # si se detecta una letra con tilde, la reemplaza por la misma pero sin ella
            cadena=cadena+"a"
        elif letra == "é" or letra=="É":
            cadena=cadena+"e"
        elif letra == "í" or letra=="Í":
            cadena=cadena+"i"
        elif letra == "ó" or letra=="Ó":
            cadena=cadena+"o"
        elif letra == "ú" or letra=="Ú":
            cadena=cadena+"u"
    return cadena                        #devuelve la cadena

def lectura(archivo, listaFrases):
    listaTodo=[]
    listaFrases1=[]
    listaTodo= archivo.readlines()   #se lee el archivo y se guaran todas sus lineas en una lista
    for elemento in listaTodo:
        if (elemento[0] != "0" and elemento[0] != "1" and elemento[0] != "2" and elemento[0] != "3" and elemento[0] != "4" and elemento[0] != "5" and elemento[0] != "6" and elemento[0] != "7" and elemento[0] != "8" and elemento[0] != "9"):
            listaFrases1.append(elemento[0:len(elemento)-1])            #si la linea no empieza con un numero, se guarda en otra lista esa linea
    for elemento in listaFrases1:                                       #se recorren las lineas que si se pueden utilizar(las que no son inservibles)
        listaFrases.append(quitarCaracteresEspeciales(elemento).lower())


#otra funcion para leer un archivo porque son muy distintos
def lectura2(archivo2, listaPalabrasDiccionario):
    listaPalabrasDiccionario= archivo2.readlines()                 #lee todas las lineas de el lemario
    for elemento in listaPalabrasDiccionario:                      #recorre todas las palabras
        elemento=quitarCaracteresEspeciales(elemento)              #Le quita los caracteres especiales

def seleccionDeLetras(palabra):
    palabra=list(palabra)                                          #pasa la palabra a lista
    if len(palabra) <= 5:                                          #para las palabras que tienen 5 letras o menos:
        for i in range(len(palabra)//3):                           #se toma un aproximadamete 30%
            pos=random.randint(0,len(palabra)-1)                   #ese 30% de letras se convierten en asteriscos en posiciones aleatorias
            palabra[pos]="*"
    else:                                                          #para las palabras de mas de 5 letras:
        for i in range(len(palabra)-5):                            #nos parecio correcto que segun las letras que tenga, la cantidad de "*" que tendra
            pos=random.randint(0,len(palabra)-1)                   #lo mismo que antes
            palabra[pos]="*"
    return palabra

def seleccionDeLetras2(palabra):                                   #Para esta funcion es lo mismo que la anterior
    palabra=list(palabra)                                          #solo que con distintos porcentajes de "*"
    if len(palabra) <= 5:
        for i in range(len(palabra)//2):
            pos=random.randint(0,len(palabra)-1)
            palabra[pos]="*"
    else:
        for i in range(len(palabra)-4):
            pos=random.randint(0,len(palabra)-1)
            palabra[pos]="*"
    return palabra

def seleccionDeLetras3(palabra):                                  #para las de 5 letras o menos:
    a=0
    palabra=list(palabra)
    if len(palabra)<= 5:
        for i in range(len(palabra)//3):
            pos=random.randint(0,len(palabra)-1)
            palabra[pos]="*"
            if a==0:                                             #Entra a este condicional
                a=1                                              #se cambia el valor de a para que solo entre una vez
                if pos==0:                                       #si la posicion aleatoria que toco es la 0, borra la siguiente letra
                    palabra.pop(pos+1)
                else:
                    palabra.pop(pos-1)                           #si es una distinta a la 0, borra la anterior
    else:
        for i in range(len(palabra)-3):
            pos=random.randint(0,len(palabra)-1)                 #lo mismo que las fuciones anteriores pero con mas dificultad
            palabra[pos]="*"
    return palabra


def nuevaPalabra(palabras):                                       #toma una palabra aleatoria de la lista y la devuelve en cadena
    pos=random.randint(0,len(palabras))
    return(PasarACadena(palabras[pos]))

def esValida(candidata, oculta, palabra):
    lista=[]
    cont=-1
    if len(candidata)==len(palabra):              #compara que tengan la misma longitud
        for letra in oculta:
            cont=cont+1
            if letra!= "*":
                lista.append(cont)             # guarda las posiciones donde no hay *
        for i in range (len(lista)):
            if candidata[lista[i]]!=palabra[lista[i]]:       #compara esas posiciones en la palabra que escribe el usuario y la que se selecciono
                return False
        return True
    return False


def musica(candidata,oculta,palabra,incorrecto,acierto, listaPalabrasPeli, listaPalabrasDiccionario):
    if esValida(candidata, oculta, palabra) and candidata==palabra:
        pygame.mixer.Sound.play(acierto)               #suena la musica si la palabra es valida
    elif not esValida(candidata,oculta,palabra) and not esta(candidata,listaPalabrasDiccionario) and not esta(candidata, listaPalabrasPeli):
        pygame.mixer.Sound.play(incorrecto)            #suena otra musica si no lo es
    else:
        pygame.mixer.Sound.play(acierto)

def procesar(candidata, oculta, palabra, listaPalabrasPeli, listaPalabrasDiccionario):            #aca implementamos la funcion puntos combinada con procesar
    if esValida(candidata, oculta, palabra) and candidata==palabra:        #si es la palabra exacta devuelve su longitud 5 veces
        return len(palabra)*5
    elif not esValida(candidata,oculta,palabra) and not esta(candidata,listaPalabrasDiccionario) and not esta(candidata, listaPalabrasPeli):
        return len(palabra)*-1                    #si no es valida devuelve su longitud negativa
    else:

        return len(palabra)                       #si no es ninguna de las anteriores devuelve solo su longitud
