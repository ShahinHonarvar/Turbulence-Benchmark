 def remove_repeat_chars(s):
    # Create a new string without any duplicates
    new_str = ""

    # Iterate through the characters in the original string
    for i in range(len(s)):
        # If the current character is not already in the new string, add it
        if s[i] not in new_str:
            new_str += s[i]

    return new_str
