from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def dividing_line():
    y = 280
    while y > -280:
        new_segment = Turtle(shape='square')
        new_segment.shapesize(0.6, 0.2, 1)
        new_segment.penup()
        new_segment.hideturtle()
        new_segment.color('white')
        new_segment.goto(x=0, y=y)
        new_segment.showturtle()
        y -= 30


game_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle(-370, 0)
r_paddle = Paddle(370, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, 'Up')
screen.onkey(l_paddle.down, 'Down')
screen.onkey(r_paddle.up, 'w')
screen.onkey(r_paddle.down, 's')
dividing_line()

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce()
    if ball.distance(l_paddle) < 40 or ball.distance(r_paddle) < 40:
        ball.deflect()
    if ball.xcor() > 405:
        ball.reset()
        scoreboard.l_point()
        l_paddle.paddle_reset()
        r_paddle.paddle_reset()
    if ball.xcor() < -405:
        ball.reset()
        scoreboard.r_point()
        l_paddle.paddle_reset()
        r_paddle.paddle_reset()
    if scoreboard.l_score == 5:
        scoreboard.l_win()
        game_on = False
    elif scoreboard.r_score == 5:
        scoreboard.r_win()
        game_on = False
screen.exitonclick()
