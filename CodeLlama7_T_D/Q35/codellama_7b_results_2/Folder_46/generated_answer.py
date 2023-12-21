
def remove_repeat_chars(string):
    # Create a set of all unique characters in the string
    char_set = set(string)
    # Iterate over each character in the set and check if it occurs more than once in the given range
    for char in char_set:
        # Get the index of the first occurrence of the character in the string
        first_index = string.index(char)
        # Get the index of the last occurrence of the character in the string
        last_index = string.rindex(char)
        # Check if the character occurs more than once between the indices 10 and 79, both exclusive
        if first_index >= 10 and last_index <= 79:
            # Remove all occurrences of the character from the string
            string = string.replace(char, '')
    return string
