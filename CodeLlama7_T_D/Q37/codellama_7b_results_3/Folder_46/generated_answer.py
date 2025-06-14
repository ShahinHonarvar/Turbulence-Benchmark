
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over the characters in the input string
    for char in string:
        # Check if the current character should be removed
        if (char >= "i" and char <= "v") or (char >= "I" and char <= "V"):
            # If so, continue to the next character in the input string
            continue

        # Otherwise, add the current character to the filtered string
        filtered += char

    # Return the filtered string
    return filtered
