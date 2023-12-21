
def remove_repeat_chars(string):
    # Get unique characters from the string
    unique_chars = list(set(string))

    # Loop through unique characters
    for char in unique_chars:
        # Check if character occurs more than once between indices 13 and 76
        if 13 < string.index(char) < 76 and string.count(char) > 1:
            # Remove all occurrences of character from string
            string = string.replace(char, '')
    
    return string
