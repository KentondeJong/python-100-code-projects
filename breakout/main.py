from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from blocks import Block

HEIGHT = 600
WIDTH = 800
ROWS = [32, 16, 8, 4]
COLOURS = ['red', 'orange', 'yellow', 'lime green']
GAP = 10
START_POSITION = (WIDTH / 2) * -1
WIDTH_MINUS_GAP = (WIDTH - (GAP * 2))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

screen.listen()
paddle = Paddle((0, -250))
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

ball = Ball()

blocks = []
int = 0

for rows in ROWS:
    for col in range(0, rows):
        blockwidth = WIDTH_MINUS_GAP / rows
        position = ((blockwidth * col) + blockwidth / 2)
        blocks.append(Block(START_POSITION + position - ((GAP / 2) - GAP), 200-(GAP * 3 * (int + 1)), blockwidth - GAP, COLOURS[int]))
    int += 1


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #paddle
    if ball.distance(paddle) <= 100 and ball.ycor() <= -250:  
       ball.setheading((ball.heading() * -1))
    #top wall
    elif (ball.ycor() >= 300 and ball.ycor() > -250):                                  
        ball.setheading((ball.heading() * -1))
    #right walls
    elif (ball.xcor() >= 400 and ball.ycor() > -250):                               
        ball.setheading((ball.heading() * 1.5))
    #left walls
    elif (ball.xcor() <= -400 and ball.ycor() > -250):                                 
        ball.setheading((ball.heading() * -1.5))
    #bottom wall
    elif (ball.ycor() <= -290):                                   
        ball.reset_position()

    for block in blocks:

        if (block.isvisible()):
            # print('-----')
            # print(abs(ball.xcor()))
            # print(abs(block.xcor()))
            # print((abs(ball.xcor()) - abs(block.xcor())))
            # print(abs(ball.ycor()))
            # print(abs(block.ycor()))
            # print((abs(ball.ycor()) - abs(block.ycor())))

            if (abs(ball.xcor()) - abs(block.xcor()) < 20) and \
            (abs(ball.ycor()) - abs(block.ycor()) < 40):
                ball.setheading((ball.heading() * -1))
                block.destroy()
                break

screen.exitonclick()