
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters and their indices
    char_dict = {}

    # Iterate over the characters in the string
    for i, c in enumerate(s):
        # If the character is already in the dictionary, remove all occurrences of it from the string
        if c in char_dict:
            start_idx = char_dict[c]
            s = s[:start_idx] + s[start_idx+1:]

        # Add the character to the dictionary with its index
        else:
            char_dict[c] = i

    return s
