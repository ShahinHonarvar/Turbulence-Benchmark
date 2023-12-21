
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters that occur between 20 and 30, inclusive
    start_index = char_list.index('a', 20)
    end_index = char_list.index('a', 30)
    # Get the list of ASCII values for the characters between the indices
    ascii_values = [ord(char) for char in char_list[start_index:end_index]]
    # Sort the list of ASCII values
    sorted_ascii_values = sorted(ascii_values)
    # Return the 8th smallest ASCII value
    return sorted_ascii_values[7]
