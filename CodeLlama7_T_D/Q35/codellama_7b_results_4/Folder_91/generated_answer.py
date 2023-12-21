 def remove_repeat_chars(s):
    # Create a new empty string
    result = ""
    # Iterate over the characters in the given string
    for c in s:
        # If the current character is not already present in the result string, append it to the result string
        if c not in result:
            result += c

    return result
