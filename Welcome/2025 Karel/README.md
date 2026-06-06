# 🤖 Karel Beeper Celebration — Code in Place 2026

A beginner Python exercise from **Stanford's Code in Place 2026**, where Karel the Robot celebrates by placing beepers across the world.

---

## 📋 Description

Karel must complete a celebratory sequence:

1. Place **20 beepers** at the starting position
2. Move **one step** to the right
3. Place **26 beepers** at the new position
4. Move **one more step** to the right, ending **facing East**

The final world looks like this:

```
+    +    +

+    +    +

[20] [26] Karel →
```

---

## 🧠 Concepts Practiced

- `put_beeper()` — places a beeper at Karel's current position
- `move()` — moves Karel one step forward
- `for` loops — repeating an action N times
- Defining helper functions (`turn_right`)

---

## 💻 Solution

```python
from karel.stanfordkarel import *

def main():
    for i in range(20):
        put_beeper()
    move()  

    for i in range(26):
        put_beeper()
    move() 

def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    main()
```

---

## ▶️ How to Run

Make sure you have the Stanford Karel library installed, then run:

```bash
python main.py
```

> **Note:** This code is designed to run inside the Code in Place online IDE at [codeinplace.stanford.edu](https://codeinplace.stanford.edu).

---

## 🐛 Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Exception: Front is blocked` | Too many `move()` calls — Karel hit a wall | Remove extra `move()` calls |
| Beepers not placed | Missing `put_beeper()` inside the loop | Make sure `put_beeper()` is indented inside the `for` block |

---

## 📚 Key Concept: For Loops

A `for` loop repeats an action a set number of times:

```python
for i in range(100):
    # this runs 100 times
    move()
```

In this exercise, we use two loops — one for each group of beepers.

---

## 🏫 Course

**Stanford Code in Place 2026**
A free, beginner-friendly Python course based on Stanford's CS106A.
🔗 [codeinplace.stanford.edu](https://codeinplace.stanford.edu)
