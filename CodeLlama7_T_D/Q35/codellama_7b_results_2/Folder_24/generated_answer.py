 def remove_repeat_chars(s):
    # Create a new string with the characters from the input string
    # that are not repeated between indices 13 and 91
    new_str = ""
    for i in range(len(s)):
        # If the current character is not repeated between
        # indices 13 and 91, add it to the new string
        if s[i] not in s[13:91]:
            new_str += s[i]
    return new_str
