<div align="center">

# 🎲 Dice Roller

### *Stanford CS106A — Python*

</div>

---

## 📋 Assignment

> Did you know that not all dice have 6 sides? You can find dice with **8 sides**, **10 sides**, and even **20 sides**.

Write a program which takes as input the **number of sides** on a dice. Then, simulate **rolling a dice** with that many sides. **Print the outcome** of the roll.

---

## ▶️ Example runs

*(user input shown in blue)*

**Example 1:**

```
How many sides does your dice have? 10
Your roll is 8
```

**Example 2:**

```
How many sides does your dice have? 100
Your roll is 76
```

---

## 🧱 Rules

| Sides | Possible outcomes |
|-------|--------------------|
| 8     | `1, 2, 3, 4, 5, 6, 7, 8` |
| 4     | `1, 2, 3, 4` |

---

## 🛠️ Function you'll need

> Recall that Python has a special function `random.randint(...)` which takes in two numbers: a **minimum value** and a **maximum value**. `randint` will return a random whole number that is **greater than or equal to the min**, and **less than or equal to the max**:

```python
random.randint(5, 9)  # returns one of [5, 6, 7, 8, 9] randomly
```

---

## 💡 Note

> You **don't** have to handle the case where the user enters an invalid number of sides (for example a `0`, a negative number, or a non-integer).

---

<div align="center">
<sub>Stanford CS106A · Karel & Python</sub>
</div>
