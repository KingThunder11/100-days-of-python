from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setheading(UP)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def go_up(self):
        """
        Moves the paddle up the screen.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        """"
        Moves the paddle down the screen.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)