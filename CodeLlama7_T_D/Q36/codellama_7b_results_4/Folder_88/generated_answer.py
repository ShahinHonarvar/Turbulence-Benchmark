
def filter_chars(string):
    # Create a new empty string
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:

        # If the current character is between the indices 78 and 81 (both exclusive) and is greater than 'S' and smaller than '[', then remove all occurrences of that character within the filtered string while keeping the order of all characters intact.
        if char == "[" or char == "]":
            continue

        elif 78 < ord(char) < 81:
            filtered_string += char

    # Return the altered string
    return filtered_string
