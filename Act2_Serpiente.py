"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

#Posición inicial de la comida
food = vector(0, 0)
#Posición inical de la serpiente
snake = [vector(10, 0)]
#Dirección inicial de la serpiente
aim = vector(0, -10)

#Listas de colores para snake y food
SnakeColor = ['blue', 'green','orange', 'purple', 'black']
FoodColor = ['blue', 'green','orange', 'purple', 'black']

#El color va a ser un valor al alzar entre las posiciones 0 y 5
i = randrange(0,5)
j = randrange(0,5)

#Ciclo para que los colores no sean iguales
while i == j:
    j = randrange(0,5)


def change(x, y):
    "Change snake direction."
    #Asigna la dirección x a aim.x    
    aim.x = x
    #Asigna la dirección y a aim.y
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    #Si la cabeza se encuentra dentro de los límites de la pantalla
        #retorna True
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    #Hace una copia del ultimo valor de snake, el cual es la cabeza
    head = snake[-1].copy()
    #Cambia el valor de Head en base a aim
    head.move(aim)

    #Verifica si la cabeza está dentro de los limites o no está dentro del cuerpo
    if not inside(head) or head in snake:
        #Genera un cuadro rojo de 9 px donde está la cabeza
        square(head.x, head.y, 9, 'red')
        #Actualiza la pantalla
        update()
        #Termina el juego
        return
    
    #Mete la nueva cabeza al final del array snake
    snake.append(head)



    #Si la cabeza se come a food (estan en la misma posicion)
    if head == food:
        #Imprime el score
        print('Snake:', len(snake))
        #Nuevas coordenadas aleatorias de la nueva comida
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        
        #Remuev el primer valor del array snake
        snake.pop(0)

    clear()

    #Por cada pieza del vector snake (body) dibuja un cuadrado con la posicion
    #X y Y
    for body in snake:
        #El color va depender del valor aleatorio de i
        square(body.x, body.y, 9, SnakeColor[i])

    #Dibuja un cuadro para la comida con las coordenadas
        #X y Y con un color aleatorio
    square(food.x, food.y, 9, FoodColor[j])
    #Actualiza la pantalla
    update()
    #La operacion se realiza cada 100 milisegundos
    ontimer(move, 100)
    
def move_food():
    #Mueve la comida una posición de forma aleatoria
    #Lista de posibles movimientos de comida
    moveList = [[10,0],[-10,0],[0,10],[0,-10],[10,10],[-10,-10],[-10,10],[10,-10]]
    #Se selecciona un movimiento al azar
    indx = randrange (0,8)
    #Se modifica el valor de comida
    food.x += moveList[indx][0]
    food.y += moveList[indx][1]

    #Verifica si en algún momento la comida está fuera
        #O está en el mismo nivel de la cabeza de tal
        #Manera de que no se lo salta
    if not inside(food) or food == snake[-1]:
        #Si se cumple cualquiera de estas condiciones la comida
            #anula el movimiento anterior y realiza el movimiento inverso
            #simulando un rebote
        if indx%2 == 0:
            food.x += moveList[indx+1][0]
            food.y += moveList[indx+1][1]
            food.x += moveList[indx+1][0]
            food.y += moveList[indx+1][1]
        else:
            food.x += moveList[indx-1][0]
            food.y += moveList[indx-1][1]
            food.x += moveList[indx-1][0]
            food.y += moveList[indx-1][1]
             
    ontimer(move_food, 600)
#Configura el tamano de la ventana y posicion de la ventana
setup(420, 420, 370, 0)
#Esconde el puntero
hideturtle()
#No dibuja el recorrido
tracer(False)
#Recibe las ordenes del teclado
listen()
#Asigna un cambio de direccion a cada tecla
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()