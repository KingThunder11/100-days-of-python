import turtle
import pandas

# setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# initialize score, correct guesses list, and read csv of all 50 states
df = pandas.read_csv("50_states.csv")
score = 0
correct_guesses = []

# initialize turtle to write state names onto screen
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

# repeat guessing prompt until 50 correct guesses
while len(correct_guesses) != 50:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                              prompt="What's another state's name?").title()

    # exits program if user gives up and creates a csv file of remaining states
    if answer == "Exit":
        remaining_states = []
        for value in df['state']:
            if value not in correct_guesses:
                remaining_states.append(value)

        new_df = pandas.DataFrame(remaining_states, columns=["Name"])
        new_df.to_csv("states_to_learn.csv")
        print(new_df)
        break

    # if guessed correctly, increases score, appends guess to correct guesses list, and writes guess onto screen
    if answer in df['state'].values:
        score += 1
        state_data = df[df['state'] == answer]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(answer)

        correct_guesses.append(answer)
