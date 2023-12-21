
def filter_chars(s):
    # Initialize a new string variable to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in s:

        # If the current character is not between indices 18 and 31, append it to the filtered string
        if not (18 < ord(char) < 31):
            filtered += char

    # Return the filtered string
    return filtered
