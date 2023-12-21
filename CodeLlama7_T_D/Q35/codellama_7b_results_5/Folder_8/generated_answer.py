 def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""
    # Iterate over the characters in the original string
    for i in range(len(s)):
        # If the character is not present in the substring, append it to the new string
        if s[i] not in s[45:48]:
            new_str += s[i]
    return new_str
