from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = file.read()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display()

    def set_score(self, score):
        self.score = score

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=("Courier", 15, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align='center', font=("Courier", 15, "normal"))

