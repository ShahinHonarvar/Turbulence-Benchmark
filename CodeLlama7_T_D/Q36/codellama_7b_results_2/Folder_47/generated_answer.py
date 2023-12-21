
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the input string
    for char in string:
        # Check if the current character is between indices 45 and 57 (exclusive)
        if 45 < ord(char) < 57:
            # If so, skip this character when building the filtered string
            continue

        # Otherwise, add the current character to the filtered string
        filtered_string += char

    return filtered_string
