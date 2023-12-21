
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Iterate over each character in the string
    for char in s:
        # If the character is not in the set of unique characters, continue to the next character
        if char not in unique_chars:
            continue

        # Otherwise, remove all occurrences of the character from the string
        else:
            s = s.replace(char, '')

    # Return the altered string

    return s
