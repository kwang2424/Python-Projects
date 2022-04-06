from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_x = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle(shape='square')
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-230, 230))
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_x, car.ycor())
            if car.xcor() < -350:
                self.cars.remove(car)

    def reset(self):
        for car in self.cars:
            car.reset()
            car.ht()
            self.cars.remove(car)
        self.move_x += MOVE_INCREMENT