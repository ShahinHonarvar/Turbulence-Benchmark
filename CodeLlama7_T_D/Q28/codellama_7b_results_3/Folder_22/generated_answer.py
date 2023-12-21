
def return_nth_smallest_ascii(string):
    # Get the characters in the string that occur between indices 0 and 16, both inclusive
    chars = set([char for char in string[0:17]])
    # Sort the characters by their ASCII values

    sorted_chars = sorted(chars, key=ord)
    # Return the character with the 17th smallest ASCII value

    return sorted_chars[16]
