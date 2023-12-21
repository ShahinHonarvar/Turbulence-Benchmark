
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters
    new_string = ""
    for i in range(len(s)):
        # Check if the current character is already in the new string
        if s[i] not in new_string:
            # If it's not in the new string, add it to the end of the new string
            new_string += s[i]
    return new_string
