# U.S. States Game - Changelog

## [0.1.0] - Setup Phase

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