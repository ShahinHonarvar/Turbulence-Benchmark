
def filter_chars(s):
    # Initialize an empty string
    result = ""

    # Iterate through the characters of the input string
    for char in s:
        # If the current character is within the specified range and satisfies the condition,
        # remove all occurrences of that character from the input string
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            result = result.replace(char, "")

    # Return the altered string
    return result
