import turtle
import time

import my_module as my

my.greeting()

turtle.speed(my_module.turtle_settings['shape'])
turtle.pensize(my_module.turtle_settings['pensize'])
turtle.pencolor(my_module.turtle_settings['pencolor'])
turtle.fullcolor(my_module.turtle_settings['fillcolor'])

turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor((0.5, 0.3, 0.9))
turtle.pencolor('#32c18f') # RRGGBB

turtle.speed('fastest')

screen = turtle.Screen()

screen.onkey(lambda: turtle.forward(15), 'w')
screen.onkey(lambda: turtle.right(5), 'd')
screen.onkey(lambda: turtle.left(5), 'a')
screen.onkey(lambda: turtle.back(15), 's')

screen.listen()
'''
turtle.forward(100)
turtle.left(90)
time.sleep(1)
turtle.pencolor('red')
turtle.back(100)
turtle.right(90)
turtle.pencolor('blue')
turtle.circle(55)

turtle.penup()
turtle.goto(-45, 60)
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(34)
turtle.end_fill()
'''
turtle.done()