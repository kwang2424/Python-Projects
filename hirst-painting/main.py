import colorgram
import turtle as t
import random


def extract(image, colors):
    colors = colorgram.extract(image, colors)
    result = []
    for color in colors:
        rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
        result.append(rgb)
    return result


color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)]
timmy = t.Turtle()
screen = t.Screen()


def draw_painting():
    t.colormode(255)
    timmy.penup()
    x = -200
    y = -200
    timmy.goto(x, y)
    for i in range(10):
        for i1 in range(10):
            color = random.choice(color_list)
            timmy.dot(20, color)
            timmy.forward(50)
        if i < 9:
            y += 50
            timmy.goto(x, y)
    screen.exitonclick()


draw_painting()