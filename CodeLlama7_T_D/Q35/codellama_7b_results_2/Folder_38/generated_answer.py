 def remove_repeat_chars(s):
    # Create a new string with the characters in the original string that do not occur more than once between indices 36 and 85
    new_str = ""
    for i, c in enumerate(s):
        if s.count(c) == 1 or i < 36 or i > 85:
            new_str += c

    # Return the altered string

    return new_str
