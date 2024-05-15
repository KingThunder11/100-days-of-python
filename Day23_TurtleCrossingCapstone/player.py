from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("green")
        self.setheading(90)
        self.shape("turtle")

    def move_up(self):
        """
        Moves the turtle up by the move distance.
        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        """
        Moves the player back to the starting position.
        """
        self.goto(STARTING_POSITION)

