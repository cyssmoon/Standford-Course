# 📦 Row of Boxes (Code in Place)

> *A Python graphics assignment from Stanford University's **Code in Place** course focused on loops, coordinate calculations, and shape styling.*

---

## 📜 About the Assignment

This exercise gives you hands-on practice with repeating graphical elements using loops and pixel calculations.

### 🎯 Objective

* Create a horizontal line of boxes that fills the bottom of the canvas.
* Each box has a fixed width and height defined by `BOX_SIZE`, totaling **5 boxes** perfectly aligned in a row.

### 🎨 Styling Individual Boxes

To ensure each box is individually visible (instead of blending into a single strip), optional arguments are passed to `create_rectangle(...)`:

* **Fill Color:** `"white"`
* **Outline Color:** `"black"`

```python
# Creates a white rectangle with a black outline
canvas.create_rectangle(
    left_x, 
    top_y, 
    right_x, 
    bottom_y, 
    "white", 
    "black"
)

```

---

## 🛠️ Implementation Details

* **For Loops:** A `for i in range(N_BOXES):` loop is used to dynamically iterate and generate each box.
* **Coordinate Math:** The loop iteration variable `i` is used to compute the changing `left_x` and `right_x` for every box in the row.

---

## 🌟 Extension: 5x5 Grid Challenge

Ready for an extra challenge once you pass the base assignment?

* Change `CANVAS_HEIGHT` to `400`.
* Use nested loops or expanded calculations to fill the **entire canvas** with a complete 5x5 grid of squares!

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Implement the `for` loop logic using `N_BOXES` and coordinate math.
3. Click the **"Check Correct"** button to verify your solution against the autograder.
