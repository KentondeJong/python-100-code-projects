from turtle import Turtle


class Block(Turtle):
    
    def __init__(self, row, column, width, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=width/20)
        self.penup()
        self.goto((row, column))

    def destroy(self):
        self.hideturtle()
