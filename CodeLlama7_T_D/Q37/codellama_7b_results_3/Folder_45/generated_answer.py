
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ''

    # Iterate over each character in the original string
    for char in s:

        # If the character is between indices 72 and 94, both inclusive, and is greater than or equal to character '.' and smaller than or equal to character 'b', then add it to the new string
        if (char >= '.' and char <= 'b') and (72 <= ord(char) <= 94):
            new_str += char

    # Return the altered string
    return new_str
