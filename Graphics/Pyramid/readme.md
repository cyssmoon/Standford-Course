# 🧱 Pyramid of Bricks (Code in Place)

> *A classic Python graphics assignment from Stanford University's **Code in Place** course focused on nested loops, layout mathematics, and scalable UI design.*

---

## 📜 About the Assignment

Your objective is to write a program that draws a brick pyramid centered at the bottom of the canvas, where each consecutive row going upward decreases by one brick.

### 📐 Constants & Parameters

The program relies on scalable constants so that changing their values automatically adjusts the entire pyramid layout:

* `BRICK_WIDTH`: The width of each brick (default: **30 pixels**).
* `BRICK_HEIGHT`: The height of each brick (default: **12 pixels**).
* `BRICKS_IN_BASE`: The number of bricks in the bottom row (default: **14**).

---

## 🛠️ Implementation & Logic

* **Nested Loops:** Use an outer loop to iterate through each row (from the base up to the top tip) and an inner loop to draw the correct number of bricks per row.
* **Centering & Alignment:** Calculate the starting X-coordinate for each row dynamically so the entire structure remains perfectly centered at the bottom of the canvas, regardless of how many bricks are in the base.
* **Scalability:** Ensure that changing `BRICK_WIDTH`, `BRICK_HEIGHT`, or `BRICKS_IN_BASE` updates the visual representation correctly without hardcoded pixel values.

---

## 💻 Code Snippet Example

Drawing an individual brick with custom fill and outline colors:

```python
canvas.create_rectangle(
    left_x, 
    top_y, 
    right_x, 
    bottom_y, 
    "yellow", 
    "black"
)

```

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Define your constants (`BRICK_WIDTH`, `BRICK_HEIGHT`, `BRICKS_IN_BASE`).
3. Implement the loop and coordinate logic to construct the pyramid from bottom to top.
4. Click **"Check Correct"** to test your solution against the autograder!
