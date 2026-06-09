# 🏛️ Temple of Artemis — Karel Column Repair

A Karel the Robot program that reconstructs the missing columns of the **Temple of Artemis in Ephesus** by placing beepers in the correct positions.

---

## 📋 Problem Description

Karel has been hired to restore the columns of the Temple of Artemis. The stones (represented by beepers) are missing from the columns that support the arches.

Karel must fill in the missing columns so the temple looks complete.

**Before:**

```
. . . . . . . . . . . . .
. . . . . . . . . . . . .
. ┌─┐ . . ┌─┐ . . ┌─┐ . .
┌─┘ └──┐ ┌─┘ └──┐ ┌─┘ └──┐
. . . . . . . . . . . . .   ← missing beepers
. . . . . . . . . . . . .
🤖 (Karel starts here)
```

**After:**

```
◇ . . . ◇ . . . ◇ . . . ◇
◇ . . . ◇ . . . ◇ . . . ◇
◇ . . . ◇ . . . ◇ . . . ◇
◇ . . . ◇ . . . ◇ . . . ◇
◇ . . . ◇ . . . ◇ . . . ◇
```

---

## 📐 World Facts

| Fact | Detail |
|------|--------|
| Starting position | Bottom-left corner, facing right (East) |
| Column positions | 1st, 5th, 9th, and 13th columns |
| Column height | 5 units |
| Distance between columns | 4 squares apart |

---

## 🧠 Solution Approach

The program uses **helper functions** to keep the code clean and readable:

- `turn_around()` — turns Karel 180°
- `construir_columna()` — places 5 beepers going upward, then returns Karel to the starting row
- `avanzar_cuatro()` — moves Karel 4 squares to the right
- `main()` — calls the above functions in sequence for all 4 columns

### Key Logic in `construir_columna()`

```
1. Turn left (face up)
2. Place beeper on current cell
3. Repeat 4 times: move up → place beeper
4. Turn around (face down)
5. Move down 4 times (back to ground level)
6. Turn left (face right again)
```

> ⚠️ The beeper is placed **before** moving to avoid hitting the top wall on the last step.


---

## 🚀 How to Run

1. Make sure you have the **Stanford Karel** library installed.
2. Place `main.py` in your Karel project folder with the `Efes` world file.
3. Run:

```bash
python main.py
```

---

## 📚 Concepts Used

- `for` loops
- Helper functions / decomposition
- Karel movement and beeper placement
- Avoiding wall collisions with careful move ordering

---

## 🏫 Course

**Lesson 4 — Art of Problem Solving**  
Stanford Karel / CodeHS
