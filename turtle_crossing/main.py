import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

scoreboard = Scoreboard()

game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_car()
    if count < 6:
        count += 1
    else:
        count = 0
        cars.new_car()
    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 280:
        player.new_level()
        scoreboard.new_level()
        cars.reset()
screen.exitonclick()