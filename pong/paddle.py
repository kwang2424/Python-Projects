from turtle import Turtle


def computer_paddle():
    comp_pad = Turtle(shape='square')
    comp_pad.shapesize(1, 4, 1)
    comp_pad.setheading(90)
    comp_pad.color('white')
    comp_pad.penup()
    comp_pad.goto(370, 0)
    comp_pad.setheading(90)
    comp_pad.penup()
    return comp_pad


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.game_start = True
        self.going_up = True
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.shape('square')
        self.shapesize(1, 4, 1)
        self.setheading(90)
        self.color('white')
        self.penup()

    def paddle_reset(self):
        self.goto(self.x, self.y)

    def up(self):
        self.forward(50)

    def down(self):
        self.forward(-50)
