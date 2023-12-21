
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between indices 18 and 31 (both exclusive)
        if 18 < ord(char) < 31:
            # And it is greater than character 'H' and smaller than character '|'
            if char > "H" and char < "|":
                # Skip this character in the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
