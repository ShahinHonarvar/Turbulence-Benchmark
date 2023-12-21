
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 60 and 88 (inclusive)
    chars = string[60:89]
    # Create a list of the ASCII values of the extracted characters
    ascii_values = [ord(char) for char in chars]
    # Sort the list in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 7th smallest ASCII value
    return sorted_ascii_values[6]
