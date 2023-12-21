
def return_nth_smallest_ascii(string):
    # Get the characters between indices 3 and 52
    chars = string[3:52]
    # Sort the characters by their ASCII value
    sorted_chars = sorted(chars, key=ord)
    # Return the 8th smallest ASCII value
    return sorted_chars[7]
