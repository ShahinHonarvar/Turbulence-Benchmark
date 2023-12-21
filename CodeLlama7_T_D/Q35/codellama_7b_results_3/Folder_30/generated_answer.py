
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the current character is repeated more than once between indices 22 and 24
        if s.count(s[i]) > 1 and i < 22 or i > 24:
            # Remove all occurrences of the current character from the string
            new_str += s[:i] + s[i+1:]
    return new_str
