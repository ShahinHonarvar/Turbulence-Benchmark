
def remove_repeat_chars(s):
    # Create a new string with the characters in the given string
    # that occur more than once between the indices 55 and 84, both exclusive, removed
    new_str = ""
    # Iterate over the characters in the given string
    for i in range(len(s)):
        # Check if the current character occurs more than once between the indices 55 and 84, both exclusive
        if s[i] in s[55:84] and s[i] not in new_str:
            # If so, remove all occurrences of that character from the given string
            new_str += s[:i] + s[i+1:]
    # Return the altered string
    return new_str
