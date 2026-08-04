def load_words_from_file(filepath):
    """
    Reads words from a file and returns them as a list.
    Assumes one word per line.
    """
    words = []
    with open(filepath, 'r') as file:
        for line in file:
            cleaned_word = line.strip()
            if cleaned_word: 
                words.append(cleaned_word)
    return words

def main():
    word_list = load_words_from_file("words.txt")
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    max_length = 0
    for word in word_counts:
        if len(word) > max_length:
            max_length = len(word)
    for word, count in word_counts.items():
        bar = 'x' * count
        print(f"{word:<{max_length}} : {bar}")

if __name__ == '__main__':
    main()
