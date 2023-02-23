from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=10)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 50
        new_x = -300 if new_x <= -300 else new_x
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 50
        new_x = 300 if new_x >= 300 else new_x
        self.goto(new_x, self.ycor())
