
def remove_repeat_chars(string):
    # Create a set of all characters in the string
    char_set = set(string)
    # Iterate over each character in the set
    for char in char_set:
        # Get the indices of all occurrences of the current character in the string
        indices = [i for i, ltr in enumerate(string) if ltr == char]
        # Remove all occurrences of the current character from the string
        for index in sorted(indices, reverse=True):
            del string[index]
    return string
