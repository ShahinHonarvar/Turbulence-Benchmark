
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate through each character in the given string
    for i, c in enumerate(s):
        # Check if the current character is between indices 75 and 99, inclusive
        if 74 < i < 100:
            # Check if the current character is greater than or equal to character '8' and smaller than or equal to character 'e'
            if c >= "8" and c <= "e":
                # Skip the current character since it needs to be filtered out
                continue

        # Add the current character to the new string
        new_str += c

    return new_str
