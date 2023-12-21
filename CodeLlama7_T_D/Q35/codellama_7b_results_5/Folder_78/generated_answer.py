
def remove_repeat_chars(s):
    # Initialize a new empty string
    result = ""

    # Iterate over each character in the input string
    for char in s:
        # If the current character is not already present in the output string
        if char not in result:
            # Append the current character to the output string
            result += char

    # Return the altered string
    return result
