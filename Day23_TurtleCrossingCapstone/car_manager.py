from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    move_increment = 10

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """
        Creates a car. Has a 1 in 6 chance of being created.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Moves the cars to the left by the move increment.
        """
        for car in self.all_cars:
            car.goto(car.xcor() - CarManager.move_increment, car.ycor())

    def increase_car_speed(self):
        """
        Increases the speed of the car by a factor of 1.4.
        """
        CarManager.move_increment = CarManager.move_increment * 1.4
