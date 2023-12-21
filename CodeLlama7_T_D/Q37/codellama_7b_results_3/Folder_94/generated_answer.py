
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the input string
    for char in s:

        # If the current character is between indices 51 and 96, both inclusive, and is greater than or equal to character 'X' and smaller than or equal to character 'p', then remove all occurrences of that character from the new string
        if (char >= 'X') and (char <= 'p'):
            continue

        # Add the current character to the new string
        new_str += char

    # Return the altered string
    return new_str
