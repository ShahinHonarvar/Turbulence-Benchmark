
def return_nth_smallest_ascii(string):
    # Extract the characters from indices 51 to 89
    chars = string[50:90]
    # Create a list of ASCII values for each character
    ascii_values = [ord(char) for char in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 14th smallest ASCII value
    return sorted_ascii_values[13]
