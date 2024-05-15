from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-215, 260)
        self.level = 1
        self.update_level()

    def update_level(self):
        """
        Writes the level text on the screen.
        """
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increment_level(self):
        """
        Increments the level by one.
        """
        self.level += 1

    def game_over(self):
        """
        Prints "game over" onto the center of the screen.
        """
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)


