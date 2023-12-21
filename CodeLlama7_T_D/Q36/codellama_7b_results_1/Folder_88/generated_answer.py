
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in string:
        # If the current character is between 78 and 81 (exclusive)
        if char >= "S" and char < "[":
            # Skip this character in the filtered string
            continue

        # Otherwise, add the current character to the filtered string
        filtered += char

    # Return the filtered string
    return filtered
