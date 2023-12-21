
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    for i in range(36, 79 + 1):
        # Check if the current character is between indices 36 and 79, both inclusive
        char = s[i]
        # Check if the current character is greater than or equal to '2' and smaller than or equal to 's'
        if ord(char) >= ord('2') and ord(char) <= ord('s'):
            # If the current character is a match, remove it from the string
            filtered = filtered + s[:i] + s[i+1:]
    # Return the altered string
    return filtered
