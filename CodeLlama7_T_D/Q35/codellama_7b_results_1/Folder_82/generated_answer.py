
def remove_repeat_chars(s):
    # Create an empty list to store the characters that need to be removed
    chars_to_remove = []
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the current character is already in the list of characters to remove
        if s[i] in chars_to_remove:
            # If it is, remove all occurrences of that character from the string
            while s[i] in s:
                s = s.replace(s[i], "")
    # Return the altered string
    return s
