from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Moves the ball along the screen.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Changes y direction of the ball when the ball hits the top and bottom
        of the screen.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Changes x direction of the ball when ball hits paddle
        """
        self.x_move *= -1

    def reset_position(self):
        """
        Resets the ball to the center of the screen after play has scored.
        Moves to the opposite player for whoever was scored on.
        """
        self.goto(0, 0)
        self.bounce_x()  # ball moves to the other player

    def increase_speed(self):
        """
        Speeds up the ball every time a paddle hits it
        """
        self.x_move *= 1.3
        self.y_move *= 1.3

    def reset_speed(self):
        """
        Resets ball speed after point has been scored and ball spawns
        back to the middle.
        """
        self.x_move = 10
        self.y_move = 10
