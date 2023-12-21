
def return_nth_smallest_ascii(s):
    # Convert string to list of characters
    char_list = list(s)
    # Calculate ASCII values for each character
    ascii_values = [ord(c) for c in char_list]
    # Find the 8th smallest ASCII value
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[7]
    return chr(nth_smallest_ascii)
