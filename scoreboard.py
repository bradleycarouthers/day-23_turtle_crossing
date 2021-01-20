from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.stage = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-255, 250)
        self.write(f"Level: {self.stage}", align="left", font=FONT)

    def new_level(self):
        self.clear()
        self.stage += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 24, "bold"))
