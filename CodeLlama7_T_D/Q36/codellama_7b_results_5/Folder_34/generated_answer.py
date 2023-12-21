
def filter_chars(s):
    # Create a new string with the desired characters removed
    new_str = ""
    for i in range(10, 80):
        # Check if the current character is greater than '?' and smaller than 'm'
        if s[i] > '?' and s[i] < 'm':
            # Skip this character
            continue

        # Append the current character to the new string
        new_str += s[i]
    return new_str
