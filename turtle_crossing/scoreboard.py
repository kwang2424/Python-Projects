from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-150, 250)
        self.level = 0
        self.write(f"Level: {self.level}", font=FONT, align='center')

    def new_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT, align='center')

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", font=FONT, align='center')
