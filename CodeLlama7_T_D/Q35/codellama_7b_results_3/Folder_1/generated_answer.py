
def remove_repeat_chars(s):
    # Create a new string with the characters from s
    # that occur once between indices 17 and 88, exclusive
    new_str = ''

    # Iterate over each character in s
    for i in range(len(s)):
        # If the current character is not already in the new string
        if s[i] not in new_str:
            # Add the current character to the new string
            new_str += s[i]

    # Return the altered string
    return new_str
