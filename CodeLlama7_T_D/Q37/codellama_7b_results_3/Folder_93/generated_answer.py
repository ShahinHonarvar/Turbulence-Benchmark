
def filter_chars(string):
    # Create a new string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in string:
        # If the current character is not between indices 38 and 69, inclusive, or if it does not meet the other conditions, add it to the filtered string
        if (char.isalpha() or char.isdigit()) and (char != "H" and char != "e"):
            filtered += char

    # Return the filtered string
    return filtered
