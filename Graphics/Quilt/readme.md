# 🧶 The Quilt Assignment (Code in Place)

> *A fun Python graphics assignment from Stanford University's **Code in Place** course focused on modular programming, functions, and coordinate systems.*

---

## 📜 About the Assignment

A quilt is a blanket composed of repeating "patches". In this project, you will write modular functions to draw different styles of patches and arrange them onto a canvas to create a complete quilt design.

### 📐 Constants & Parameters
* **Patch Dimensions:** Each patch has a fixed width and height of 100 pixels, defined by `PATCH_SIZE`.
* **Standard Function Signature:** Every patch function takes the exact same three parameters:
  * `canvas`: The canvas upon which we are drawing.
  * `start_x`: The left side coordinate of the patch in pixels.
  * `start_y`: The top side coordinate of the patch in pixels.

---

## 🛠️ Development Milestones

* **Milestone 1: Circle Patch**  
  Implement the missing `draw_circle_patch(canvas, start_x, start_y)` function. You will draw a circle that fills the patch at the specified location (e.g., colored `'salmon'`).
* **Milestone 2: Second Row**  
  Update the `main()` function to add four more lines of code to draw the second row of patches. Remember that the second row will have a `start_y` value equal to `PATCH_SIZE` (100 pixels from the top).
* **Milestone 3: Collaborate & Create**  
  Design your own custom patch function keeping the 100x100 size restriction and share it with your peers on the course forum!

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Complete the `draw_circle_patch` function body.
3. Add the second row function calls inside `main()`.
4. Click **"Check Correct"** to test your solution against the autograder!
