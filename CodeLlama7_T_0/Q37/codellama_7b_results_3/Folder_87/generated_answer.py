
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 18 and 81, both inclusive, and is greater than or equal to character 'W' and smaller than or equal to character '['
        if (char >= "W" and char <= "[") and (18 <= len(string) and len(string) <= 81)):
            # If the current character meets the criteria, do not add it to the filtered string
            continue

        # Otherwise, add the current character to the filtered string
        filtered_string += char

    # Return the altered string with the filtered characters
    return filtered_string
