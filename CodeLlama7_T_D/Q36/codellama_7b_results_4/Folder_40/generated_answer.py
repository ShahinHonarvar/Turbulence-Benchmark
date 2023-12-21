
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between the indices 1 and 7 (both exclusive)
        if 1 < char < 7:
            # Remove all occurrences of the current character from the filtered_string
            filtered_string = filtered_string.replace(char, "")
        else:
            # Add the current character to the filtered_string
            filtered_string += char

    return filtered_string
