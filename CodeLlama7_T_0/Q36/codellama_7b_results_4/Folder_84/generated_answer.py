
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between indices 171 and 636 (both exclusive)
        if 170 < ord(char) < 637:
            # And it is greater than character 'c' and smaller than character 's'
            if char > "c" and char < "s":
                # Skip this character in the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
