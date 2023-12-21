
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character is between indices 72 and 94, both inclusive
        if (i >= 72 and i <= 94) and (char >= '.' and char <= 'b'):
            # Remove all occurrences of the current character from the string
            char_list = [x for x in char_list if x != char]
    # Join the list of characters back into a string and return it
    return "".join(char_list)
