
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Loop through each character in the given string
    for char in string:
        # If the current character is between indices 52 and 81, both inclusive, and is greater than or equal to 'A' and smaller than or equal to 'U', then remove all occurrences of that character from the string while preserving the order of all characters in the string.
        if 52 <= char <= 81:
            # Replace all occurrences of the current character with an empty string, while preserving the order of all characters in the string.
            filtered = filtered.replace(char, "")

    # Return the altered string
    return filtered
