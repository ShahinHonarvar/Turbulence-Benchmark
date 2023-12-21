
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate through each character in the input string
    for char in s:

        # If the current character is between indices 41 and 79, both inclusive, and is greater than or equal to character 'f' and smaller than or equal to character '|', then add it to the filtered string.
        if (41 <= ord(char) <= 79) and ('f' <= char <= '|'):
            filtered += char

    # Return the filtered string
    return filtered
