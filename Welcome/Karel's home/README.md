# Karel Collects Food 🏠🤖

A Karel the Robot program where Karel leaves her house, picks up a beeper (food), and returns to her starting position. This is an assignment from Stanford's [Code in Place](https://codeinplace.stanford.edu) course focused on **decomposition**.

## Description

Karel starts in the corner of her house, facing east. A beeper (representing food) is placed just outside the doorway. The program instructs Karel to:

1. Move to the beeper (outside the door)
2. Pick it up
3. Return to her starting position

## How to Run

1. Open the Karel editor (the `main.py` tab)
2. Paste the code below
3. Click the **Run** button

## Expected Result

After running the program, Karel will be back in her starting corner inside the house, and the beeper will be gone (Karel picked it up).

```
+    +    +    +    +
     ___________
+   |🤖   +    |    +
    |           |
+   |  +    +  |    +
    |___________|
+    +    +    +    +
```

## Concepts Used

- `move()` — moves Karel one step forward
- `pick_beeper()` — picks up a beeper from the current tile
- `turn_left()` — turns Karel 90° to the left
- **Decomposition** — breaking the solution into smaller helper functions (`move_to_beeper`, `return_home`, `turn_around`)

## Resources

- 📖 [Karel Reader (Chapters 1–4)](https://codeinplace.stanford.edu)
- 💬 [Public Discussion Forum](https://codeinplace.stanford.edu/public/forum)
