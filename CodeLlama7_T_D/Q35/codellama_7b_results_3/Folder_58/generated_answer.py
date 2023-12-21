 def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 103 and 802, both exclusive
    new_string = ""
    for i in range(len(s)):
        # If the character at index i is not already in the new string
        if s[i] not in new_string:
            # Add the character to the new string
            new_string += s[i]
    return new_string
