 def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the original string
    for char in string:
        # Check if the current character should be removed
        if (char >= "O") and (char <= "^"):
            continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
