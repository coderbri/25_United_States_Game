# 25 U.S. States Game

<!-- TODO: create a readme for this project containing an overview, the concepts implemented, the project logic, and finally acknowledgements that it was an inspiration of an online guessing quiz game () built as part of a Python learning journey through Angela Yu's 100 Days of: Python Pro Bootcamp -->


## Overview

The game displays a blank outline of the United States. Users are prompted to input state names via a text box. When a correct state is guessed, it is labeled directly on the map. The game continues until all 50 states are correctly named or the user types `"Exit"`.

At the end, any missed states are saved to a `states_to_learn.csv` file for further study.

---

## Concepts Implemented

- **Python Turtle Graphics** for GUI visualization
- **Event-driven logic** using `while` loops and user input prompts
- **Data handling** with `pandas` to load state names and coordinates
- **CSV export** for unguessed states
- **Basic string and list manipulation** for comparison logic
- **Dynamic text rendering** on a custom-shaped screen (map)

---

## Project Logic

1. Load a blank map image (`blank_states_img.gif`) using Turtle.
2. Read `50_states.csv` into a list using `pandas`.
3. Prompt the user to guess a state name.
4. If the guess is valid and not already guessed:
   - Retrieve the x and y coordinates of the state.
   - Display the state name at the appropriate location.
5. Repeat until:
   - All 50 states are guessed, or
   - The user types `"Exit"`.
6. If exited early, export all remaining unguessed states to `states_to_learn.csv`.

<div align="center">
<img src="assets/25_demo.gif"
   alt="Demo of U.S. States Guessing Game"
   width="450px" height="auto">
</div>

---

## How to Run (in PyCharm)

1. **Open Project** 
   - Open the `25_US_States_Game` project in PyCharm.
2. **Install Dependencies** 
   - Make sure pandas is installed:
     ```py
     pip install pandas
     ``` 
3. **Run the Game**
   - Right-click `main.py` and select Run it as the current file. 
   - The U.S. map will appear—start guessing state names!

---

## Acknowledgements

Inspired by a U.S. states guessing quiz and implemented as part of a Python learning journey through Dr. Angela Yu’s 100 Days of Code: Python Pro Bootcamp.

---
<section align="center">
  <code>coderBri © 2025</code>
</section>