# 🌪️ Hailstone Sequence (Collatz Conjecture) in Python

> *An interactive console program exploring the famous Collatz Conjecture from Douglas Hofstadter’s Pulitzer-prize-winning book, **Gödel, Escher, Bach**.*

---

## 📜 About the Problem

The **Hailstone Sequence** (also known as the **Collatz Conjecture**) is one of the most famous unsolved problems in mathematics. The process follows a simple set of rules for any positive integer $n$:

1. If $n$ is **even**, divide it by 2 ($n / 2$).
2. If $n$ is **odd**, multiply it by 3 and add 1 ($3n + 1$).
3. Continue this process until $n$ is equal to 1.

Just like hailstones carried up and down by winds before falling to the ground, the numbers in this sequence go up and down unpredictably before eventually culminating at 1 (for every number tested to date!).

---

## 💻 Example Output

Here is what the program output looks like for an input of `15`:

```text
Enter a number: 15
15 is odd, so I make 3n + 1: 46
46 is even, so I take half: 23
23 is odd, so I make 3n + 1: 70
70 is even, so I take half: 35
35 is odd, so I make 3n + 1: 106
106 is even, so I take half: 53
53 is odd, so I make 3n + 1: 160
160 is even, so I take half: 80
80 is even, so I take half: 40
40 is even, so I take half: 20
20 is even, so I take half: 10
10 is even, so I take half: 5
5 is odd, so I make 3n + 1: 16
16 is even, so I take half: 8
8 is even, so I take half: 4
4 is even, so I take half: 2
2 is even, so I take half: 1
```

---

## 🛠️ Implementation Details

* **Even/Odd Check:** Uses the modulo operator (`% 2`) to determine if a number is even or odd.
* **Integer Casting:** Division in Python turns numbers into floats (e.g., `4 / 2 = 2.0`), so results are cast back to integers (`int()`) to match autograder expectations.
* **Step Tracking:** Counts and displays the total number of steps taken until $n = 1$.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed.

### Running the Program
1. Clone or download this repository.
2. Run the script from your terminal:
   ```bash
   python hailstone.py
   ```
