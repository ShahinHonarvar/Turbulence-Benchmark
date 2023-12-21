
def return_nth_smallest_ascii(string):
    # Get the characters between indices 18 and 45 (inclusive)
    chars = string[18:46]
    # Get the ASCII values of the characters
    ascii_values = [ord(c) for c in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 7th smallest ASCII value
    return chars[sorted_ascii_values.index(7)]
