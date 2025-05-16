import pandas
import turtle

# * --- Screen Setup ---
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the U.S. map image
image = "assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data from CSV and convert to list
data = pandas.read_csv("assets/50_states.csv")
all_states = data.state.to_list()
guessed_states = []     # If user types "Exit", generate a list of missing states and save to CSV

# * --- Game Loop ---
while len(guessed_states) < 50:
    # Prompt user and format guess
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()
    print(answer_state)

    # If user types "Exit", generate a list of missing states and save to CSV
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        print("Creating CSV file for unguessed states...")
        unguessed_states = pandas.DataFrame(missing_states)
        unguessed_states.to_csv("states_to_learn.csv")
        print("CSV file created!")
        break

    # If guess is valid, record and display it on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]

        # Create turtle to write state name on map
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(state_data.x.item(), state_data.y.item())
        marker.write(answer_state)
