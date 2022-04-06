from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.screen_write()

    def l_point(self):
        self.l_score += 1
        self.screen_write()

    def screen_write(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, font=("Fixedsys", 80, "normal"), align='center')
        self.goto(100, 180)
        self.write(self.r_score, font=("Fixedsys", 80, "normal"), align='center')

    def r_point(self):
        self.r_score += 1
        self.screen_write()

    def r_win(self):
        self.goto(0, 0)
        self.write("Player 2 Wins!", font=("Fixedsys", 80, "normal"), align='center')

    def l_win(self):
        self.goto(0, 0)
        self.write("Player 1 Wins!", font=("Fixedsys", 80, "normal"), align='center')

