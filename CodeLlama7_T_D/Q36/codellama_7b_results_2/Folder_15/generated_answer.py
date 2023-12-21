
def filter_chars(s):
    # Create a new string with the same characters as the input string
    new_str = ''
    # Iterate over the characters in the input string
    for char in s:
        # If the character is between indices 2 and 7 (both exclusive) and is greater than 'h' and smaller than 'k', remove all occurrences of that character within the string while keeping the order of all characters intact.
        if char not in ['h','i','j','k'] and char < 'k' and char > 'h':
            new_str += char
    # Return the altered string
    return new_str
