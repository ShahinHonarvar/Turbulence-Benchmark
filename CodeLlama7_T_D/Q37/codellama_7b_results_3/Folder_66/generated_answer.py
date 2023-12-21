
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Initialize a new empty string to store the filtered characters
    filtered_string = ""

    for i in range(27, 85 + 1):
        # Check if the current character is greater than or equal to 'c' and smaller than or equal to 'i'
        if char_list[i] >= 'c' and char_list[i] <= 'i':
            # Skip this character since it meets the conditions
            continue

        # If we reach here, then the current character does not meet the conditions
        # So, add it to the filtered string
        filtered_string += char_list[i]

    return filtered_string
