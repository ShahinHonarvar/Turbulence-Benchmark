
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters and their indices
    char_dict = {}

    # Iterate over the string and update the dictionary with the character and its index
    for i, c in enumerate(s):
        if c not in char_dict:
            char_dict[c] = [i]
        else:
            char_dict[c].append(i)

    # Iterate over the dictionary and remove all occurrences of characters that appear more than once between indices 38 and 81, both exclusive
    for c, indices in char_dict.items():
        if len(indices) > 1:
            for i in sorted(indices)[-2::]:
                s = s[:i] + s[i+1:]

    # Return the altered string
    return s
