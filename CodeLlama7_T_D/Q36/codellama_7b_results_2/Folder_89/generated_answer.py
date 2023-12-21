
def filter_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Iterate over the characters between indices 57 and 69 (both exclusive)
    for i in range(57, 69):
        # If the current character is greater than '(' and smaller than 'W', remove all occurrences of that character within the string while keeping the order of all characters intact.
        if char_list[i] > '(' and char_list[i] < 'W':
            # Replace the current character with an empty space to remove it from the string.
            char_list[i] = ' '
    # Join the list of characters back into a string and return it.
    return ''.join(char_list)
