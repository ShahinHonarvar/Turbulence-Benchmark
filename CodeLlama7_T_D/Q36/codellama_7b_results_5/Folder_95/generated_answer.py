
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the given string
    for c in s:
        # If the current character is not between 56 and 86 (exclusive) or if it is less than '+' or greater than 'w', then add it to the filtered string
        if c < "5" or c > "8" or c == "+":
            filtered += c

    # Return the filtered string
    return filtered
