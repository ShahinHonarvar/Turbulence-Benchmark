
def return_nth_smallest_ascii(string):
    # Find the characters in the string between indices 38 and 64 (inclusive)
    chars = string[38:65]
    # Sort the characters by their ASCII value
    sorted_chars = sorted(chars, key=ord)
    # Return the character with the 14th smallest ASCII value
    return sorted_chars[13]
