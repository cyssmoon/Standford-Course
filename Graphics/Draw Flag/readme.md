# 🇮🇩 Drawing Flags: Indonesia (Code in Place)

> *An introductory Python graphics assignment from Stanford University's **Code in Place** course, celebrating an international class of students from 150 different countries!*

---

## 📜 About the Assignment

To celebrate the global diversity of the Code in Place community, this assignment introduces Python graphics by having students draw national flags. 

We kick off with one of the most straightforward flags to draw: **The Flag of Indonesia**.

### 📐 Dimensions & Constants
The canvas dimensions are governed by these predefined constants:
* `CANVAS_WIDTH = 450`
* `CANVAS_HEIGHT = 300`

### 🎨 Core Logic
* The Indonesian flag consists of two equal horizontal bands: red on top and white on the bottom.
* Since the default canvas background is already white, all you need to do is draw a **single red rectangle** covering the top half of the canvas!

---

## 💻 Code Snippet Example

Using the provided graphics method for drawing colored rectangles:

```python
# Draws a rectangle with specified color
rect = canvas.create_rectangle(
    left_x, 
    top_y, 
    right_x, 
    bottom_y,
    color
)
```

---

## 🌟 Creative Extension: Design Your Own Flag!

Once you pass the autograder for the Indonesian flag, get creative:
* Design your own custom flag representing your friends, family, or a community/group that doesn't have an official flag yet.
* Experiment with shapes, lines, circles, and colors using Python graphics.

---

## 🚀 Getting Started

1. Open your Code in Place IDE / workspace.
2. Complete the logic to draw the red top half of the Indonesian flag.
3. Click the **"check correct"** button underneath the canvas to test your code against the autograder!
