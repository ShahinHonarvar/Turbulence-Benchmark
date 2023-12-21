
def filter_chars(string):
    # Create a new empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the input string
    for char in string:
        # If the character is between 32 and 84 (both exclusive) and is not 'm' or 'w', add it to the filtered string
        if (char != "m" and char != "w") and (32 < ord(char) < 84):
            filtered_string += char

    # Return the filtered string
    return filtered_string
