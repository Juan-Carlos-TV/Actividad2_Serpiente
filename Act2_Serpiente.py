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
    #X y Y de 9 pixeles yd e color negro
    for body in snake:
        square(body.x, body.y, 9, 'black')

    #Dibuja un cuadro para la comida con las coordenadas X y Y de 9 pixeles y de color verde
    square(food.x, food.y, 9, 'green')
    #Actualiza la pantalla
    update()
    #La operacion se realiza cada 100 milisegundos
    ontimer(move, 100)
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
done()