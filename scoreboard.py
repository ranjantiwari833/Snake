from turtle import Turtle
from constants import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-20,SCREEN_HEIGHT/2 - 20)
        self.write("Score: {}".format(self.score),False,ALIGNMENT,FONT)
    
    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0,70)
        self.write("GAME OVER\nScore: {}".format(self.score),False,ALIGNMENT,FONT)
    
    def score_update(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score),False,ALIGNMENT,FONT)
        
