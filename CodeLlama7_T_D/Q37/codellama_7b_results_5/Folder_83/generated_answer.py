 def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""
    # Iterate over each character in the input string
    for char in s:
        # Check if the current character is between indices 29 and 79, inclusive
        if 29 <= ord(char) <= 79:
            # Check if the current character is greater than or equal to 'K' and smaller than or equal to 'z'
            if 'K' <= char <= 'z':
                # Skip this character since it should be removed from the string
                continue

        # Add the current character to the new string
        new_str += char
    # Return the altered string
    return new_str
