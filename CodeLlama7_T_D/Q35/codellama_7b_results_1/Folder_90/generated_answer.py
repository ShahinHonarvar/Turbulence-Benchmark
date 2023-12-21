
def remove_repeat_chars(s):
    # Create a new string that will contain the characters from s, but with all repeated characters removed
    new_str = ""
    # Iterate over each character in s
    for i in range(len(s)):
        # If the current character is not already present in the new string
        if s[i] not in new_str:
            # Add it to the new string
            new_str += s[i]
    # Return the altered string
    return new_str
