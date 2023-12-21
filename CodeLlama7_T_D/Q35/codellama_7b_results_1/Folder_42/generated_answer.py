
def remove_repeat_chars(s):
    # Create a new string with the characters of the original string
    # excluded from the repeated characters range
    new_str = ""

    # Iterate over the characters in the string
    for i in range(len(s)):
        # Check if the current character is not in the
        # repeated characters range
        if i < 18 or i > 60:
            # Add the current character to the new string
            new_str += s[i]

    # Return the altered string
    return new_str
