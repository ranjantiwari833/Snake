from turtle import Turtle
import random
from constants import *

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        self.refresh()
    
    def refresh(self):    
        xrange = (SCREEN_WIDTH/2)-30
        yrange = (SCREEN_HEIGHT/2)-30
        random_x = random.randint(-xrange,xrange)
        random_y = random.randint(-yrange,yrange)
        
        self.goto(random_x,random_y)