
def remove_repeat_chars(string):
    # Create a list of characters from the given string
    char_list = list(string)

    # Iterate through the characters in the list
    for i in range(len(char_list)):
        # If the current character is repeated between indices 86 and 89, exclusive
        if char_list[i] in string[85:90]:
            # Remove all occurrences of the current character from the string
            string = string.replace(char_list[i], '', 1)
    return string
