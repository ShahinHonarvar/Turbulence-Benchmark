
def remove_repeat_chars(s):
    # Create a new string with all repeating characters removed
    new_str = ""
    for i in range(len(s)):
        # If the current character is not already in the new string
        if s[i] not in new_str:
            # Add the current character to the new string
            new_str += s[i]
    return new_str
