
def remove_repeat_chars(s):
    # Create a dictionary to store the characters and their indices
    char_dict = {}

    # Iterate over the string and create a dictionary of characters and their indices
    for i, c in enumerate(s):
        if c not in char_dict:
            char_dict[c] = [i]

        else:

            char_dict[c].append(i)

    # Iterate over the dictionary and remove all occurrences of characters that occur more than once between indices 20 and 35
    for c in char_dict:
        if len(char_dict[c]) > 1:
            indices = char_dict[c]

            # Sort the list of indices in ascending order
            sorted_indices = sorted(indices)

            # Remove all occurrences of the character from the string, while preserving the order of all characters in the string
            for i in reversed(sorted_indices):
                s = s[:i] + s[i+1:]
    return s
