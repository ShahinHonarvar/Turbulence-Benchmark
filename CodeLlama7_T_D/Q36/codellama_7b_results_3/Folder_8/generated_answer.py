
def filter_chars(string):
    # Create a new list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the string
    for char in string:
        # Check if the current character is between the indices 82 and 93 (both exclusive)
        if 82 < ord(char) < 93:
            # If it is, check if it is greater than '!' and smaller than '*'
            if char > "!" and char < "*":
                # If it is, do not add it to the filtered characters list
                continue

        # Add the current character to the filtered characters list
        filtered_chars.append(char)
    # Return the altered string with all occurrences of characters between indices 82 and 93 (both exclusive) removed while keeping the order of all characters intact
    return "".join(filtered_chars)
