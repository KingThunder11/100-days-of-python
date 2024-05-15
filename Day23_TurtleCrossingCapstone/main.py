import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# screen listens to up key for player
screen.listen()
screen.onkey(player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # moves the cars and creates a car every refresh (1 in 6 chance)
    car_manager.move_cars()
    car_manager.create_car()

    # detect if the player reaches the top of the screen (finish line)
    if player.ycor() > 280:
        scoreboard.increment_level()
        scoreboard.update_level()
        player.reset_position()
        car_manager.increase_car_speed()

    # detect if the player collides with a car
    cars = car_manager.all_cars
    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
