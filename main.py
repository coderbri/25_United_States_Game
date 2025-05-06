import turtle
from turtle import Turtle, Screen

# --- Screen Setup ---
screen = Screen()
screen.title("U.S. States Game")

# Load U.S. map image as background shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --- Note ---
# We don't need to manually capture coordinates with mouse clicks,
# because the CSV file used will contain all necessary state coordinates.

# Example: Getting mouse click coordinates (not needed for final version)
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# --- Popup Input Setup ---
# This is just a test prompt. Later, we'll trigger it based on user clicks.

# --- Popup Input Setup ---
# This is just a test prompt. Later, we'll trigger it based on user clicks.
answer_state = screen.textinput(
    title="Guess the State",
    prompt="What's another state's name?"
)
print(answer_state)

# --- Keep Screen Open ---
# Option 1: Keeps the window open and allows further interaction
# turtle.mainloop()

# Option 2: Keeps screen open until user clicks (common for testing)
# screen.exitonclick()

# TODO: Only show text input popup when a state is clicked