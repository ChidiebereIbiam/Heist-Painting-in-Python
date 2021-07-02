# import colorgram
#
# colors = colorgram.extract('download.jpeg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# Heist Multimillion Painting using Python
# Author - Ibiam Chidiebere Orji

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(238, 224, 81), (205, 4, 74), (199, 164, 8), (238, 48, 132), (206, 75, 12), (109, 180, 219),
              (218, 161, 104), (235, 224, 4), (28, 190, 109), (11, 24, 64), (20, 107, 176), (15, 28, 178),
              (218, 133, 179), (7, 186, 216), (228, 167, 200), (211, 24, 151), (120, 191, 159), (7, 50, 26),
              (60, 21, 7), (125, 219, 234), (32, 136, 71), (192, 13, 4), (108, 88, 215), (141, 217, 202), (238, 63, 35),
              (69, 10, 27)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()