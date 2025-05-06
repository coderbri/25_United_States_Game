# U.S. States Game - Notes

## 🐢 Turtle Screen Behavior: Keeping the Window Open

### Why the Turtle window stays open without `exitonclick()` or `mainloop()`

- The method `screen.textinput()` is **blocking**, meaning it pauses the program and holds the window open while waiting for user input.
- During this blocking state, the internal event loop continues running, keeping the Turtle screen interactive and visible.
- Once the user submits input or closes the dialog, the script continues or ends.

### When do you need `exitonclick()` or `mainloop()`?

| Method           | Purpose                                      | Blocks Script? | Keeps Window Open? |
|------------------|----------------------------------------------|----------------|---------------------|
| `textinput()`    | Prompt user for input via popup              | ✅ Yes         | ✅ While active      |
| `exitonclick()`  | Keeps screen open until user clicks          | ✅ Yes         | ✅ Until clicked     |
| `mainloop()`     | Starts event loop for interactive programs   | ✅ Yes         | ✅ Indefinitely      |

### Tip
When replacing `textinput()` with click-based input, you will need to use `turtle.mainloop()` or `screen.exitonclick()` to keep the game running and allow ongoing interaction.