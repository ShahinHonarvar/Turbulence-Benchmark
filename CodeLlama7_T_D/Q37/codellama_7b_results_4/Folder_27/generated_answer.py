
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate over the characters in the original string
    for char in s:

        # Check if the character is between indices 43 and 80, both inclusive, and is greater than or equal to character '=' and smaller than or equal to character 'E'
        if (char >= '=' and char <= 'E') and (43 <= char < 81):

            # If the character is in this range, do not include it in the new string
            continue

        # Otherwise, include the character in the new string
        new_string += char

    return new_string
