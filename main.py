import pandas
import turtle

# * --- Screen Setup ---
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load U.S. map image as background shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read state data and convert to list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []                 # ✓ 5. Record the correct guesses in a list

# * --- Game Loop ---
while len(guessed_states) < 50:     # ✓ 4. Use a loop to allow the user to keep guessing
    # Prompt user and format guess
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",   # ✓ 6. Keep track of the score
        prompt="What's another state's name?"
    ).title()                       # ✓ 1. Convert the guess to Title case
    print(answer_state)

    # Validate guess and record if correct
    if answer_state in all_states:  # ✓ 2. Check if the guess is among the 50 states
        guessed_states.append(answer_state)

        # Display state name on map at correct coordinates
        state_data = data[data.state == answer_state]
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(state_data.x.item(), state_data.y.item())
        marker.write(answer_state)  # ✓ 3. Write correct guesses onto the map

screen.exitonclick()
