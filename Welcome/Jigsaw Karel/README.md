# Karel Completes the Puzzle 🧩🤖

A Karel the Robot program where Karel picks up the last puzzle piece (a beeper), places it in the correct spot on the puzzle grid, and returns to her starting position. Assignment from Stanford's [Code in Place](https://codeinplace.stanford.edu) course.

## Description

Karel has almost completed a beeper puzzle inside a walled grid. The last piece sits on row 1, column 3 (outside the puzzle area). Karel needs to:

1. **Move to and pick up** the last puzzle piece (row 1, column 3)
2. **Place it** in the correct position (row 3, column 4) inside the puzzle
3. **Return** to the bottom-left corner facing East

## How to Run

1. Open the Karel editor (the `main.py` tab)
2. Paste the code below
3. Click the **Run** button

## Expected Result

After running the program, the puzzle grid is fully filled with beepers and Karel is back at the bottom-left corner facing East.

```
+    +    +    +    +    +    +
     ________________________
+   |  💎  💎  💎  💎  |   +
    |                        |
+   |  💎  💎  💎  💎  |   +
    |                        |
+   |  💎  💎  💎  💎  |   +
    |                        |
+   |  💎  💎  💎  💎  |   +
    |________________________|
+    +    +    +    +    +    +

🤖→  +    +    +    +    +    +
```

## Concepts Used

- `move()` — moves Karel one step forward
- `pick_beeper()` — picks up a beeper from the current tile
- `put_beeper()` — places a beeper on the current tile
- `turn_left()` — turns Karel 90° to the left
- **`turn_right()`** — custom helper built from three `turn_left()` calls
- **Decomposition** — solution split into `pick_up_piece()`, `place_piece()`, and `return_home()`

## Resources

- 📖 [Karel Reader (Chapters 1–4)](https://codeinplace.stanford.edu)
- 💬 [Public Discussion Forum](https://codeinplace.stanford.edu/public/forum)
