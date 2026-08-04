# 🧠 Memory List Game (Code in Place)

> *An interactive Python memory card matching game assignment from Stanford University's **Code in Place** course, built step-by-step using lists, loops, random shuffling, and user input validation.*

---

## 📜 About the Assignment

This project guides you through creating a classic **Memory Card Game** in Python. Cards are represented as numbers inside a list, and their board locations correspond directly to the list indices.

---

## 🛠️ Development Milestones

* **Milestone 1: Create the Truth List**
Use a `for` loop to create a master list containing pairs of numbers from `0` to `NUM_PAIRS - 1` (e.g., if `NUM_PAIRS = 3`, the list is `[0, 0, 1, 1, 2, 2]`).
* **Milestone 2: Shuffle the List**
Import Python's `random` library and use `random.shuffle(truth)` to randomize the placement of the numbers, printing the result to verify.
* **Milestone 3: Create a Displayed List**
Keep track of a parallel board state displayed to the user using `'*'` symbols to hide unrevealed cards, matching the total length of the truth list.
* **Milestone 4: Get a Valid Index**
Write input validation logic (wrapped in a `get_valid_index` function) to ensure the user inputs an index within board boundaries that hasn't already been revealed.
* **Milestone 5: Check for Matches**
Prompt for two valid, distinct indices. If they match, reveal the numbers on the display board; if not, show the values briefly before hiding them again.
* **Milestone 6: Play Multiple Turns & Win Condition**
Loop the game until all pairs are successfully located, clearing the terminal between turns and declaring victory with a congratulatory message.

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Build your program incrementally following Milestones 1 through 6.
3. Test your game logic by playing through matches and verifying error handling for invalid or duplicate indices.
4. Click **"Check Correct"** to submit your solution!
