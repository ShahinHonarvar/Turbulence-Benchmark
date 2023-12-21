
def filter_chars(string):
    # Split the string into individual characters
    chars = list(string)

    # Loop through each character in the string
    for i, char in enumerate(chars):
        # Check if the current character is between indices 22 and 85, both inclusive
        if (i >= 22 and i <= 85) and (char >= '7' and char <= 'e'):
            # If it is, remove all occurrences of that character from the string
            chars = [c for c in chars if c != char]

    # Join the list of characters back into a string
    filtered_string = "".join(chars)

    # Return the altered string
    return filtered_string
