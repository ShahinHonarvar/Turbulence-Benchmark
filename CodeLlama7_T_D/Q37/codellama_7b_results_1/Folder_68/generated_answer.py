
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate through each character in the original string
    for char in s:

        # Check if the current character should be removed
        if (char >= "6") and (char <= "w"):
            continue

        # Add the character to the new string
        new_string += char

    # Return the filtered string
    return new_string
