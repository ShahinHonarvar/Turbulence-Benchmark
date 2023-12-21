
def remove_repeat_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate through each character in the string and check if it occurs more than once between indices 10 and 76
    for i, char in enumerate(char_list):
        if char_list.count(char) > 1 and (i >= 10 and i <= 76):
            # Remove all occurrences of the character from the string
            while char_list.count(char) > 0:
                char_list.remove(char)

    # Join the list of characters back into a string and return it
    return ''.join(char_list)
