
def filter_chars(string):
    # Create a new string with all characters removed
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 283 and 484 (both exclusive)
        if 283 < ord(char) < 484:
            # If so, remove all occurrences of this character within the filtered_string while keeping the order of all characters intact.
            filtered_string = filtered_string.replace(char, "", 1)

        # Add the current character to the filtered string if it does not meet the conditions above
        else:
            filtered_string += char

    return filtered_string
