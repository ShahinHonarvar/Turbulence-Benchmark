
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    result = ""

    # Iterate over each character in the given string
    for c in s:
        # Check if the current character is between 1 and 6 (both exclusive)
        if 1 < ord(c) < 7:
            # If so, remove all occurrences of that character from the result string
            result = result.replace(c, "")
        else:
            # Otherwise, add the current character to the result string
            result += c

    return result
