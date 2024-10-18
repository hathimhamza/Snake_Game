from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
         super(). __init__()
         self.color("white")
         self.score=0
         self.penup()
         self.goto(0,275)
         self.write(f"Score : {self.score}", align="center", font=("Arial",15,"normal"))
         self.hideturtle()

    def score_add(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 15, "normal"))








