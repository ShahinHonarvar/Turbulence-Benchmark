
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the ASCII values of all the characters in the string
    ascii_values = [ord(char) for char in char_list]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Get the 4th smallest ASCII value
    nth_smallest_ascii = sorted_ascii_values[3]
    return chr(nth_smallest_ascii)
