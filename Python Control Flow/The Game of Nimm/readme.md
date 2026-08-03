# 🎮 Nimm Game in Python

> *A beautiful, interactive implementation of the ancient strategy game **Nimm**.*

---

## 📜 About the Game

**Nimm** (from the old German word *"nehmen"*, meaning "take") is an ancient mathematical game of strategy. It is also known as **Tiouk Tiouk** in West Africa and **Tsynshidzi** in China.

### 🎲 Core Rules
* **The Pile:** The game starts with a pile of **20 stones** between two players.
* **Turns:** Players take turns alternating between **Player 1** and **Player 2**.
* **Movements:** On each turn, a player may remove either **1 or 2 stones** from the center pile.
* **The Catch:** The game continues until all stones are gone. **The last player to take a stone loses.**

---

## 🛠️ Project Development Milestones

This project is structured progressively into manageable milestones, making it ideal for learning and clean coding:

* **Milestone 1: Basic Loop & Input**  
  Starts with 20 stones, loops through the removal process, and prints remaining stones until zero without worrying about player turns or input validation.
* **Milestone 2: Turn Tracking**  
  Introduces a variable to keep track of turns, alternating prompts between Player 1 and Player 2 dynamically.
* **Milestone 3: Input Validation**  
  Ensures robust gameplay by validating user input using a `while` loop, forcing players to enter valid numbers (1 or 2) if they try illegal moves.
* **Milestone 4: Winner Announcement**  
  Detects when the final stone is taken and correctly declares the winner according to the "misère" play convention (the loser takes the last stone, meaning the other player wins!).

---

## 🌟 Awesome Extensions & Features

Want to level up your project? Try implementing these custom extensions:

* 🤖 **AI Opponent:** Add a computer player mode (start with random moves, then build a smart strategic AI!).
* 🔢 **Customizable Take Limit:** Expand the rules to allow players to take 1, 2, or **3** stones per turn.
* ⚖️ **Variant Win Conditions:** Let users choose whether taking the last stone wins or loses the game.
* ⚡ **The Divisible by 3 Rule:** If the number of stones remaining at the end of a player's turn is divisible by 3, they get an extra turn!
* 🛡️ **Single-Stone Safety Rule:** If only 1 stone is left, enforce that the player *must* take it.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your machine.

### Running the Game
1. Clone or download this repository.
2. Open your terminal or command prompt in the project directory.
3. Run the script:
   ```bash
   python nimm.py
   ```

---

