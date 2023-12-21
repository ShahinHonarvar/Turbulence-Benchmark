
def remove_repeat_chars(s):
    # Initialize an empty string to store the altered string
    result = ""

    # Iterate over each character in the given string
    for i in range(len(s)):
        # If the current character is not a repeat of a previous character, add it to the result string
        if s[i] not in result:
            result += s[i]

    # Return the altered string
    return result
