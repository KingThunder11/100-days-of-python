import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
# right paddle controls
screen.onkey(right_paddle.go_up, key="Up")
screen.onkey(right_paddle.go_down, key="Down")
# left paddle controls
screen.onkey(left_paddle.go_up, key="w")
screen.onkey(left_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()




screen.exitonclick()