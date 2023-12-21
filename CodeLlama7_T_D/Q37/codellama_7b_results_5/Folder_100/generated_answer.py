
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over the characters in the original string
    for char in string:

        # Check if the character is between indices 88 and 90, both inclusive
        if (88 <= ord(char) <= 90):

            # Check if the character is greater than or equal to 'J' and smaller than or equal to 'Q'
            if ('J' <= char <= 'Q'):

                # Skip this character since it needs to be filtered out
                continue

        # Add the character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
