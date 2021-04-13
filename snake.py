from turtle import Turtle
from constants import *

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake(color="orange")
        self.head = self.body[0]
        self.head.color("orange")
    
    def create_snake(self,cor=STARTING_POSITION,color="white"):
        for position in cor:
            self.add_segment(position,color)

    def add_segment(self,position,color="white"):
        segment = Turtle(shape="square")
        segment.color(color)
        segment.penup()
        segment.goto(position)
        self.body.append(segment)
    
    def extend(self):
        self.add_segment(self.body[-1].position(),color="orange")
    
    def move(self):
        for seg in range(len(self.body)-1,0,-1):
            new_x = self.body[seg-1].xcor()
            new_y = self.body[seg-1].ycor()
            self.body[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)
    
    def right(self):
        if self.body[0].heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.body[0].heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)