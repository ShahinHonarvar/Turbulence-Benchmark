
def remove_repeat_chars(s):
    # Create a new string with the characters of s in order
    result = ""

    # Iterate over each character in s
    for c in s:

        # If the current character is not already in result, append it to the end of result
        if c not in result:
            result += c

    # Return the altered string
    return result
