
def remove_repeat_chars(s):
    # Initialize a new string to store the altered characters
    result = ""

    # Iterate over each character in the original string
    for i, c in enumerate(s):
        # If the current character occurs more than once between indices 10 and 28
        if s.count(c) > 1 and i >= 10 and i < 28:
            # Remove all occurrences of that character from the string
            result += c * (s.count(c) - 1)

    # Return the altered string
    return result + s[i:]
