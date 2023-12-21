
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is within the specified range and meets the condition, remove it from the filtered string
        if (char >= "O" and char <= "d") and (char >= 28 and char <= 65):
            continue

        # Otherwise, append the current character to the filtered string
        else:
            filtered_string += char

    # Return the filtered string
    return filtered_string
