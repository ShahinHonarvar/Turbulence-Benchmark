
def return_nth_smallest_ascii(string):
    # Get the ASCII values of all characters in the string
    ascii_values = [ord(char) for char in string]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value
    return sorted_ascii_values[5]
