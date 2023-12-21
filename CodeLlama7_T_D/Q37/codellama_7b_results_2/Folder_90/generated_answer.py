
def filter_chars(s):
    # Create a set of all characters in the given string
    char_set = set(s)
    # Iterate over each character in the given string
    for c in s:
        # If the current character is between indices 348 and 852, both inclusive
        if 348 <= s.find(c) <= 852 and c >= 'J' and c <= 'b':
            # Remove all occurrences of the current character from the string
            char_set.remove(c)
    # Return the altered string with all filtered characters removed
    return ''.join(char_set)
