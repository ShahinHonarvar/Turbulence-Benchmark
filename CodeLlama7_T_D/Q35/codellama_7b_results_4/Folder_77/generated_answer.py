
def remove_repeat_chars(s):
    # Create a set of all characters in the string
    char_set = set(s)
    # Iterate over the characters in the string
    for c in s:
        # If the character appears more than once between the indices 355 and 988, exclusive
        if c in char_set and s.count(c) > 1 and not (s.index(c) >= 355 and s.index(c) <= 988):
            # Remove all occurrences of the character from the string
            s = s.replace(c, "")
    return s
