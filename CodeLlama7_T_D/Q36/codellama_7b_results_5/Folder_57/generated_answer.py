
def filter_chars(string):
    # Create a new string with the same characters as the original string
    filtered_string = ""

    # Iterate over each character in the string
    for char in string:

        # If the current character is between 70 and 74 (exclusive)
        if ord(char) > 70 and ord(char) < 75:

            # Remove all occurrences of this character from the filtered string
            filtered_string = filtered_string.replace(char, "")

    return filtered_string
