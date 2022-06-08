'''
Jose Manuel Arango 74863
Juan Esteban Alzate 64852
Jhoan Sebastian Ortiz 
Juan Esteban Castillo 68234
'''

from re import S
import numpy as np
import turtle
from Nodo import Nodo
from email.mime import image

juego = np.array([])
juego = np.loadtxt('matriz.txt', skiprows=0)  # Carga del txt

# 0=robot,1=roca,2=espacios disponibles,3=tiburon,4=torguda,5=dori,6=marlin,7=nemo,Acuaman=8
wn = turtle.Screen()  # crea la pantalla de la interfaz
wn.title("Juego de buscando a nemo")  # Le da el titulo a la ventana
wn.setup(width=500, height=500)  # le da las dimesiones a la ventana
wn.bgcolor('sky blue')  # le da el color de fondo

robot = turtle.Turtle()  # crea el objeto turtle a la ventana

dot_distance = 55  # distancia entre puntos
robot.speed(50)  # velocidad de dibujado
robot.penup()  # levanta la pluma
robot.goto(-200, 200)  # cordenas de inicio para pintar

for i in range(0, juego.shape[0]):
    for j in range(0, juego.shape[1]):

        robot.pendown()  # bajar la pluma

        if juego[i, j] == 0:
            robot.fillcolor('blue')  # rellena los cuadrados de color azul
        if juego[i, j] == 1:
            robot.fillcolor('coral')  # rellena los cuadrados de color azul
        if juego[i, j] == 2:
            robot.fillcolor('green')  # rellena los cuadrados de color azul
        if juego[i, j] == 3:
            robot.fillcolor('beige')  # rellena los cuadrados de color azul
        if juego[i, j] == 4:
            robot.fillcolor('azure')  # rellena los cuadrados de color azul
        if juego[i, j] == 5:
            robot.fillcolor('DarkGray')  # rellena los cuadrados de color azul
        if juego[i, j] == 6:
            # rellena los cuadrados de color azul
            robot.fillcolor('aquamarine')
        if juego[i, j] == 7:
            robot.fillcolor('pink')  # rellena los cuadrados de color azul
        if juego[i, j] == 8:
            robot.fillcolor('black')  # rellena los cuadrados de color azul

        robot.begin_fill()  # empieza a pintar
        robot.forward(50)  # traza una linea 50 pixeles
        robot.right(90)  # gira 90 grados el dibujado       
        robot.forward(50)
        robot.right(90)
        robot.forward(50)
        robot.right(90)
        robot.forward(50)
        robot.right(90)
        robot.end_fill()  # finaliza el rellenado
        robot.penup()  # termina de pintar
        robot.forward(dot_distance)  # separa los los dibujos del pinsel

    robot.backward(dot_distance*juego.shape[1])  # permite regresar al inicio el pinsel

    # permite que el pinsel baje (recuadros)
    robot.right(90)
    robot.forward(dot_distance)
    robot.left(90)

def busqueda_profundidad(juego):
    global robot
    for i in range(0, juego.shape[0]):
        for j in range(0, juego.shape[1]):
            if juego[i, j] == 0:
                post_bot = (i, j)
                juego[i, j] = 2  # Colocar la posición como un espacio libre
                break  # Salga del for

    raiz = Nodo(
        juego,
        post_bot,
        (False, False, False),
        [post_bot],
        [post_bot]

    )
    pila = [raiz]

    nodos_expandidos = 1
    nodos_creados = 1
    resultado=0
    while True:

        nodo = pila.pop(-1)  # quito el primero elemento
        nodos_expandidos += 1
        # Condicion de ganar
        if nodo.verificar_ganar():
            resultado = nodo.recorrido
            break

        hijos = nodo.generar_hijos()
        for h in hijos:
            if not(h.verificar_perdi()):  # Solo evaluo nodos en cuales no pierdo
                pila.append(h)
            nodos_creados += 1
        # Condición de no encontrar
        if len(pila) == 0:
            resultado=None
            break
    
    array1 = resultado
    
    dot_distance = 55  # distancia entre puntos
    robot.penup()  # levanta la pluma
    robot.goto(-200, 200)
    print(array1)
    for i in range(0, juego.shape[0]):
        for j in range(0, juego.shape[1]):                  
         

            if (j, i)  in array1:
            #if True:
                robot.pendown()  # bajar la pluma                
                robot.fillcolor('blue')  # rellena los cuadrados de color azul
                robot.begin_fill()  # empieza a pintar
                robot.forward(50)  # traza una linea 50 pixeles
                robot.right(90)  # gira 90 grados el dibujado                
                robot.forward(50)
                robot.right(90)
                robot.forward(50)
                robot.right(90)
                robot.forward(50)
                robot.right(90)
                robot.end_fill()  # finaliza el rellenado

                robot.penup()  # termina de pintar
                robot.forward(dot_distance)  # separa los los dibujos del pinsel
            else:
                               
                robot.forward(50)  # traza una linea 50 pixeles
                robot.right(90)  # gira 90 grados el dibujado
                # se repite para completar el cuadrado
                robot.forward(50)
                robot.right(90)

                robot.forward(50)
                robot.right(90)

                robot.forward(50)
                robot.right(90)
                                
                robot.forward(dot_distance)  # separa los los dibujos del pinsel

        robot.backward(dot_distance*juego.shape[1])  # permite regresar al inicio el pinsel

    # permite que el pinsel baje (recuadros)
        robot.right(90)
        robot.forward(dot_distance)
        robot.left(90)

busqueda_profundidad(juego.copy())
turtle.done()  # termina el trabajo
# termina el trabajo
