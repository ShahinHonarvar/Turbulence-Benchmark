
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate through the characters in the list and remove any characters that are between indices 31 and 70 (both exclusive) and greater than character 'B' and smaller than character 'v'
    for i, char in enumerate(char_list):
        if i >= 31 and i < 70 and ord(char) > ord('B') and ord(char) < ord('v'):
            char_list.remove(char)
    # Return the altered string
    return ''.join(char_list)
