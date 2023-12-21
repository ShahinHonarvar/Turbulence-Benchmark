
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters
    char_dict = {}

    # Iterate over the string and update the dictionary
    for c in s:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1

    # Remove repeated characters from the string
    for c, count in char_dict.items():
        if count > 1:
            s = s.replace(c, '')

    return s
