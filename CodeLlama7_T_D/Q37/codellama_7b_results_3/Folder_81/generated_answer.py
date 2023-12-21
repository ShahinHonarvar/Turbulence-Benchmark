
def filter_chars(string):
    # Initialize an empty string
    filtered = ""

    # Iterate over each character in the input string
    for char in string:

        # Check if the current character should be removed
        if (char >= "8" and char <= "m") and (char.isdigit() or char.isalpha()):
            continue

        # Add the filtered character to the output string
        filtered += char

    # Return the filtered string
    return filtered
