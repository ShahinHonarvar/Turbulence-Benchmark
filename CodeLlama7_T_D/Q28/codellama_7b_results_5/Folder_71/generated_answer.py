
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 5 and 82
    chars = string[5:82]
    # Convert the characters to ASCII values
    ascii_values = [ord(char) for char in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 16th smallest ASCII value
    return sorted_ascii_values[15]
