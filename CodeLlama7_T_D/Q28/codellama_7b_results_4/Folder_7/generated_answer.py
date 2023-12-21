
def return_nth_smallest_ascii(string):
    # Create a list of the ASCII values of each character in the string
    ascii_values = [ord(char) for char in string]
    # Get the indices of the characters that occur between 12 and 55
    indices = [index for index, value in enumerate(ascii_values) if 12 <= value <= 55]
    # Sort the ASCII values based on their indices
    sorted_ascii_values = sorted(ascii_values, key=indices.index)
    # Return the character with the 17th smallest ASCII value
    return chr(sorted_ascii_values[16])
