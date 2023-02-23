from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.setheading(290)   

    def move(self):
        self.forward(1)  

    def block_bounce(self):
        self.setheading(random.randint(45, 135))
        self.forward(1)   

    def reset_position(self):
        self.goto(0, 0)
