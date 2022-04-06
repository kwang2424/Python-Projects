from turtle import Turtle
import time
import random
x_move = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        random_x = random.randint(10, 15)
        random_y = random.randint(10, 15)
        x_choices = [random_x, -random_x]
        y_choices = [random_y, -random_y]
        self.move_x = random.choice(x_choices)
        self.move_y = random.choice(y_choices)

    def move(self) -> object:
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def deflect(self):
        self.move_x *= -1

    def reset(self):
        self.goto(0, 0)
        random_x = random.randint(10, 15)
        random_y = random.randint(10, 15)
        x_choices = [random_x, -random_x]
        y_choices = [random_y, -random_y]
        self.move_x = random.choice(x_choices)
        self.move_y = random.choice(y_choices)
        time.sleep(0.5)


