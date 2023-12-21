
def return_nth_smallest_ascii(string):
    # Get the characters in the string
    chars = list(string)
    # Get the ASCII values of the characters
    ascii_values = [ord(c) for c in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value
    return sorted_ascii_values[5]
