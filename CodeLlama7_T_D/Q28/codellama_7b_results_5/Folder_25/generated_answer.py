
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between 34 and 68
    start_index = string.find('a', 34)
    end_index = string.rfind('z', 68)
    # Create a list of the ASCII values for the characters in the string between the start and end indices
    ascii_values = [ord(char) for char in string[start_index:end_index]]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 6th smallest ASCII value in the list
    return sorted_ascii_values[5]
