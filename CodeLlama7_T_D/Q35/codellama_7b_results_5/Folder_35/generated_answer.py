
def remove_repeat_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Iterate over each character in the list
    for i, c in enumerate(char_list):
        # If the current character occurs more than once between indices 77 and 84
        if s.count(c) > 1 and i >= 77 and i < 84:
            # Remove all occurrences of the current character from the string
            char_list = [x for x in char_list if x != c]
    # Return the altered string
    return "".join(char_list)
