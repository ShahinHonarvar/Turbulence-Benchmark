
def filter_chars(string):
    # Create a new string with the desired characters removed
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # If the current character is between 1 and 6 (exclusive) and is not ',' or 'f', then remove all occurrences of that character from the filtered string
        if 1 < ord(char) < 6 and char not in ["'", "f"]:
            filtered_string = filtered_string.replace(char, "")

    # Return the altered string
    return filtered_string
