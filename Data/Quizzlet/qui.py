def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    for english_word, correct_spanish in translations.items():
        user_answer = input(f"What is the Spanish translation for {english_word}? ")
        if user_answer.strip().lower() == correct_spanish:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {correct_spanish}.")
        print()
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")

if __name__ == '__main__':
    main()
