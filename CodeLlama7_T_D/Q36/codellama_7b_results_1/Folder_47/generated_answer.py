
def filter_chars(string):
    # Create a list of characters between indices 45 and 57
    char_list = string[45:57]
    # Remove all occurrences of each character in the list from the original string
    for char in char_list:
        string = string.replace(char, '')
    return string
