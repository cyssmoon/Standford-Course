<div align="center">

# 🔁 Double Until 100

### *Stanford CS106A — Python*

</div>

---

## 📋 Assignment

> Write a program that asks a user to **enter a number**. Your program will then **double that number** and **print out the result**. It will repeat that process until the value is **100 or greater**.

---

## ▶️ Example run

*(user input shown in blue)*

```
Enter a number: 2
4
8
16
32
64
128
```

> **Note that:**
> 2 doubled is 4
> 4 doubled is 8
> 8 doubled is 16
> ...and so on.
>
> We stop at **128** because that value is greater than **100**.

---

## 🛠️ Hints

Maintain the current number in a variable named `curr_value`. When you double the number, you should be updating `curr_value`. Recall that you can double the value of `curr_value` using a line like:

```python
curr_value = curr_value * 2
```

This program should have a **while loop**, and the loop condition should test if `curr_value` is **less than 100**. Thus, your program will have the line:

```python
while curr_value < 100:
```

---

<div align="center">
<sub>Stanford CS106A · Karel & Python</sub>
</div>
