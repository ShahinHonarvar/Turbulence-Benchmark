
def remove_repeat_chars(string):
    # Loop through each character in the string
    for i in range(2, 7):
        char = string[i]
        # Check if the current character occurs more than once between indices 2 and 7
        if string.count(char) > 1:
            # Remove all occurrences of the current character from the string
            string = string.replace(char, "")
    return string
