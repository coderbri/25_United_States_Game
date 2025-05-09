# U.S. States Game - Changelog

## [0.1.0] - Setup Phase
Date: 2025-05-05

### Added
- Created main project file and initialized Turtle screen
- Added U.S. blank map image (`blank_states_img.gif`) as shape
- Setup a test `textinput()` popup to prompt for state name
- Confirmed `textinput()` works with basic submission and printing
- Added optional methods (`mainloop`, `exitonclick`) to keep the screen open for interaction

### Notes
- Mouse click coordinate function was tested but is not needed due to coordinate data in the CSV file
- Use `turtle.mainloop()` if building a click-based state guessing mechanic
- Next step: Only trigger the popup input when user clicks on a state

---

## [0.2.0] - Game Logic Implementation
Date: 2025-05-07

### Added
- Implemented main game loop to handle user guesses.
- Displayed correct state names on map using coordinate data from CSV.
- Tracked number of correct guesses and updated window title accordingly.

### Changed
- Cleaned up comments for readability and structure.
- Ensured guesses are case-insensitive and matched using `.title()` format.

### Fixed
- Prevented duplicate entries from being added to the guessed states list.

---

## [0.3.0] - Exit Logic & Learning Feature
Date: 2025-05-09

### Added
- Implemented "Exit" keyword to allow the user to end the game early.
- Added logic to compare guessed states with full state list.
- Generated `states_to_learn.csv` file containing unguessed states for further study.

### Changed
- Refined comments throughout the code for improved clarity and conciseness.
- Replaced `.exitonclick()` with logic-driven loop termination using user input.

### Notes
- This update turns the game into a learning tool by providing feedback on missed states.
- The CSV output can be used to build follow-up features, such as quiz review or repetition mode.