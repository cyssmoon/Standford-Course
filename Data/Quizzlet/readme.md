# 🇪🇸 Spanish Vocabulary Quizzer (Code in Place)

> *An interactive Python vocabulary quiz assignment from Stanford University's **Code in Place** course, designed to practice dictionaries, loops, and user input handling while celebrating global language learning.*

---

## 📜 About the Assignment

Code in Place brings together a massive and diverse student body from all around the world. To celebrate and practice language skills, this project builds a helpful study tool to quiz users on Spanish translations using Python dictionaries.

### 🎯 Objective

* Loop through a dictionary containing English words and their corresponding Spanish translations.
* Prompt the user to enter the Spanish translation for each word.
* Check if the user's answer is correct, provide immediate feedback, and keep a running count of correct answers.
* Separate each question and answer with a blank line for visual clarity.
* Display a final score summary at the end of the quiz.

---

## 💻 Sample Run

Here is what an interactive session of the program looks like:

```text
What is the Spanish translation for hello? hola
That is correct!

What is the Spanish translation for dog? gato
That is incorrect, the Spanish translation for dog is perro.

... (quizzes user on the rest of the words)
That is correct!

You got 6/8 words correct, come study again soon!

```

---

## 🛠️ Implementation Details

* **Dictionaries:** Uses a Python dictionary (`dict`) where keys are English words and values are their Spanish translations.
* **For Loops:** Iterates through the dictionary items to present each word to the user.
* **Conditionals:** Compares user input against the dictionary value to check correctness and handle feedback branches.
* **Score Tracking:** Increments a counter variable each time a user answers correctly, culminating in a final ratio display.

---

## 🚀 Getting Started

1. Open your Code in Place IDE workspace.
2. Initialize your dictionary with English-Spanish word pairs.
3. Implement the loop, input prompts, feedback checks, and final score tally.
4. Click **"Check Correct"** to test your solution against the autograder!
