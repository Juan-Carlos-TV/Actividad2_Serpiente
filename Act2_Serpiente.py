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

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()