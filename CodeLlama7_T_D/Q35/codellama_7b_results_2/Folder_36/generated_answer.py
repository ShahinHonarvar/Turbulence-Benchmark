
def remove_repeat_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Loop through each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character occurs more than once between indices 476 and 709
        if char_list.index(char) != i:
            # Remove all occurrences of the current character from the string
            char_list = [x for x in char_list if x != char]
    return ''.join(char_list)
