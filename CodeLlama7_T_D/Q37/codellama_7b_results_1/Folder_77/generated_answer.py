
def filter_chars(my_string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in my_string:
        # Check if the current character is between indices 384 and 411, both inclusive
        if 384 <= ord(char) <= 411:
            # Check if the current character is greater than or equal to '/' and smaller than or equal to '8'
            if char >= "/" and char <= "8":
                # Skip this character since it meets the condition for removal
                continue

        # If we reach here, it means the current character does not meet the condition for removal. Therefore, we add it to the filtered string.
        filtered_string += char

    return filtered_string
