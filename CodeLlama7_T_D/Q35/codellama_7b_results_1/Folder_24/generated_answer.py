
def remove_repeat_chars(s):
    # Create a new string that is the same length as the original string
    new_str = s * len(s)
    # Iterate through each character in the original string
    for i, char in enumerate(s):
        # If the current character occurs more than once between indices 13 and 91
        if s.count(char) > 1 and i >= 13 and i <= 91:
            # Remove all occurrences of the current character from the new string
            new_str = new_str.replace(char, "")
    return new_str
