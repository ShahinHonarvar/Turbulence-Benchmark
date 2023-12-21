
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate through each character in the string
    for i in range(len(s)):

        # Check if the current character occurs more than once between indices 125 and 825, both exclusive
        if s.count(s[i]) > 1 and i < 125 or i > 825:

            # Remove all occurrences of the current character from the string
            new_str += s[:i] + s[i+1:]

    # Return the altered string
    return new_str
