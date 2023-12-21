
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over each character in the original string
    for char in s:
        # Check if the current character is between indices 31 and 70 (exclusive)
        if 31 < ord(char) < 70:
            # Check if the current character is greater than 'B' and smaller than 'v'
            if char > 'B' and char < 'v':
                # Skip this character since it needs to be removed
                continue

        # Append the current character to the new string
        new_str += char

    return new_str
