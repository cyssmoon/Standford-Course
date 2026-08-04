# 👶 Baby Vocabulary Histogram (Code in Place)

> *An engaging data-processing assignment from Stanford University's **Code in Place** course focused on dictionaries, file data, and text-based data visualization.*

---

## 📜 About the Assignment

Parenthood brings the exciting milestone of hearing a baby's first words! To explore a baby's developing vocabulary, this program reads a list of words spoken by a baby from an external file, counts how many times each word appears, and generates a text-based histogram.

### 📊 Histogram Formatting

* **Vertical Labels:** Each unique word appears vertically down the left side.
* **Horizontal Bars:** Each occurrence of a word is represented by a singular `'x'` character stretching horizontally.

---

## 💻 Sample Output

Here is what your program's console output should look like:

```text
mama    : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
dada    : xxxxxxxxxxxxxxxxxxxxxxxxxx
baba    : xxxxxxxxxxxxxxx
bye-bye : xxxxxxxxxxxxxxxxxxxx
hi      : xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
no      : xxxxxxxxxxxxxxx
juice   : xxxxxxxxxx
please  : xxxxxxx
apple   : xxxxx

```

---

## 🛠️ Implementation Details

* **File Reading:** The starter code automatically loads a list of spoken words from a file into a list structure.
* **Frequency Counting:** Use a Python dictionary (`dict`) to tally up how many times each unique word occurs in the dataset.
* **String Multiplication:** Use loops combined with string repetition (`'x' * count`) to draw the horizontal bars cleanly next to their respective words.

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Check the file icon to explore the loaded list of baby words.
3. Implement the dictionary counting logic and the histogram formatting loop.
4. Click **"Check Correct"** to verify your solution against the autograder!
