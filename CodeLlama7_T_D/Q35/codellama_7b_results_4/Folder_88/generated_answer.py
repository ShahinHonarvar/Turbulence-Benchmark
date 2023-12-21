
def remove_repeat_chars(s):
    # Create a new string without repeating characters
    result = ""

    # Iterate through the characters in the original string
    for char in s:

        # If the character is not already in the result string, append it
        if char not in result:
            result += char

    return result
