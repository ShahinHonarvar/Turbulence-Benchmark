
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # If the current character is between indices 52 and 81 (inclusive) and is greater than or equal to 'A' and smaller than or equal to 'U', then append it to the filtered string
        if 52 <= ord(c) <= 81 and c >= "A" and c <= "U":
            filtered += c

    # Return the filtered string

    return filtered
