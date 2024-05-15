import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setting up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # hides animations

# creating instances
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

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

    # detect ball collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # detect if ball goes past right player's paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_increment()
        scoreboard.update()
        ball.reset_speed()

    # detect if ball goes past left player's paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_increment()
        scoreboard.update()
        ball.reset_speed()

screen.exitonclick()