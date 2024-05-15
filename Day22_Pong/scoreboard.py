from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        """
        Clears the previous text and updates the scoreboard with the
        new score.
        """
        self.clear()
        self.write(f"Left: {self.left_score} Right: {self.right_score}", align=ALIGNMENT, font=FONT)

    def right_increment(self):
        """
        Increases the score of the right player by one.
        """
        self.right_score += 1

    def left_increment(self):
        """
        Increases the score of the left player by one.
        """
        self.left_score += 1