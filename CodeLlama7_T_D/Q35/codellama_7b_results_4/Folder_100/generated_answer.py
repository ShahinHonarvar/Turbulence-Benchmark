
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_string = ""

    # Iterate through each character in the given string
    for i in range(len(s)):
        # Check if the current character is repeated more than once between indices 44 and 78
        if s.count(s[i]) > 1 and i < 44 or i > 78:
            # Remove all occurrences of the current character from the given string
            new_string += s[:i] + s[i+1:]
    return new_string
