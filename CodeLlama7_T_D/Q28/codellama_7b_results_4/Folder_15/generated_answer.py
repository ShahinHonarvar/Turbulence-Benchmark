
def return_nth_smallest_ascii(string):
    # Split the string into a list of characters
    char_list = list(string)
    # Get the ASCII values of all characters in the string
    ascii_values = [ord(c) for c in char_list]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value
    return sorted_ascii_values[5]
