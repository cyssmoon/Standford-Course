import random

NUM_PAIRS = 3

# NOTE: Your starter code might already import or define clear_terminal(). 
# If it does, you can delete this helper function to avoid duplicates!
def clear_terminal():
    # A simple way to clear the screen by printing blank lines
    print('\n' * 20)

def get_valid_index(displayed_list, first_index=-1):
    """
    Prompts the user for an index and validates it based on game rules.
    Loops until a valid index is provided.
    """
    while True:
        user_input = input("Enter an index: ")
        try:
            idx = int(user_input)
        except ValueError:
            print("Not a number. Try again.")
            continue
        if idx < 0 or idx >= len(displayed_list):
            print("Invalid index. Try again.")
            continue
        if idx == first_index:
            print("You entered the same index twice. Try again.")
            continue
        if displayed_list[idx] != '*':
            print("This number has already been matched. Try again.")
            continue     
        return idx

def main():
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
    random.shuffle(truth_list)
    displayed_list = ['*'] * (NUM_PAIRS * 2)
    while '*' in displayed_list:
        print(displayed_list)
        index1 = get_valid_index(displayed_list)
        index2 = get_valid_index(displayed_list, first_index=index1) 
        if truth_list[index1] == truth_list[index2]:
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
            print("Match!")
            clear_terminal()
        else:
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue... ")
            clear_terminal()
    print(displayed_list)
    print("Congratulations! You won!")

if __name__ == '__main__':
    main()
