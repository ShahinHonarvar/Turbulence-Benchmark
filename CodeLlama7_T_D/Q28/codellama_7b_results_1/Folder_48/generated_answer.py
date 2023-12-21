
def return_nth_smallest_ascii(s):
    # Extract the characters between indices 37 and 59
    chars = s[37:59]
    # Get the ASCII values of the extracted characters
    ascii_values = [ord(c) for c in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value
    return chr(sorted_ascii_values[5])
