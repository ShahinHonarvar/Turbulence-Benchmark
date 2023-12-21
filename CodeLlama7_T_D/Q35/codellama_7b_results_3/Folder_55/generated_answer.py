
def remove_repeat_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Iterate through each character in the list
    for i, c in enumerate(char_list):
        # Check if the current character occurs more than once between indices 10 and 100
        if s.count(c) > 1 and i >= 10 and i < 100:
            # Remove all occurrences of the current character from the list
            char_list = [x for x in char_list if x != c]
    # Join the list of characters back into a string
    return "".join(char_list)
