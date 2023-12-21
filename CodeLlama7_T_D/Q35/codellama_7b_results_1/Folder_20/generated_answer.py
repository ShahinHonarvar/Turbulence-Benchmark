
def remove_repeat_chars(string):
    # Create a set of all characters in the given string
    char_set = set(string)
    # Iterate over each character in the set and check if it occurs more than once between indices 27 and 96
    for char in char_set:
        # If the character occurs more than once between these indices, remove all occurrences of it from the string
        if string.count(char) > 1 and (string.index(char) > 26 or string.index(char) < 96)):
            string = string.replace(char, '')
    return string
