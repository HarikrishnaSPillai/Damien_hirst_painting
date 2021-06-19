import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
colors = [(198, 198, 32), (250, 250, 17), (39, 39, 189), (38, 38, 67), (238, 238, 5), (229, 229, 46), (27, 27, 158), (215, 215, 12), (15, 15, 16), (199, 199, 10), (242, 242, 252), (244, 244, 165), (229, 229, 122), (73, 73, 31), (60, 60, 8), (224, 224, 211), (222, 222, 8), (10, 10, 61), (17, 17, 43), (47, 47, 232), (11, 11, 239), (79, 79, 215), (237, 237, 222), (73, 73, 169), (78, 78, 201), (50, 50, 244), (3, 3, 40), (222, 222, 44), (174, 174, 231), (5, 5, 222), (251, 251, 48), (235, 235, 164)]

tim.setheading(220)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)