
def return_nth_smallest_ascii(string):
    # Get the indices of the characters between 25 and 88
    start_index = string.find('{') + 1
    end_index = string.rfind('}') - 1
    # Create a list of the ASCII values of the characters in the specified range
    ascii_values = [ord(c) for c in string[start_index:end_index] if ord(c) >= 25 and ord(c) <= 88]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the character with the 11th smallest ASCII value
    return chr(sorted_ascii_values[10])
