
def remove_repeat_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)

    # Iterate through each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character occurs more than once between indices 20 and 200
        if char_list[max(i-19, 0)] == char and char_list[min(i+19, len(char_list)-1)] == char:
            # Remove all occurrences of the current character from the string
            for j in range(len(char_list)):
                if char_list[j] == char:
                    del char_list[j]

    # Join the list of characters back into a string and return it
    return "".join(char_list)
