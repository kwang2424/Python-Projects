from turtle import Turtle
move_distance = 20
up = 90
down = 270
left = 180
right = 0
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(0)

    def move(self):
        for body_num in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[body_num - 1].xcor()
            next_y = self.segments[body_num - 1].ycor()
            self.segments[body_num].goto(next_x, next_y)
        self.head.forward(move_distance)

    def reset(self):
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]