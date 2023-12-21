
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in s:
        # Check if the current character is between the indices 24 and 37 (both exclusive)
        if ord(char) >= 24 and ord(char) < 37:
            # If it is, skip adding it to the filtered string
            continue

        else:

            # Otherwise, add the current character to the filtered string
            filtered_string += char

    # Return the filtered string
    return filtered_string
