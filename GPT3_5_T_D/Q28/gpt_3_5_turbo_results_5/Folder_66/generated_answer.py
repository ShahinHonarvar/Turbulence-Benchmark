
def return_nth_smallest_ascii(string):
    subset = string[35:53]
    ascii_values = [ord(char) for char in subset]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[9])  # Return the 10th smallest ASCII value character
