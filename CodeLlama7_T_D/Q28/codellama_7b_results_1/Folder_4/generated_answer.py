
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 9 and 22
    start_index = string.find('a', 9)
    end_index = string.find('z', 22)
    # If no characters occur between these indices, return None
    if start_index == -1 or end_index == -1:
        return None

    # Get the ASCII values of all the characters in the string that occur between these indices
    ascii_values = [ord(char) for char in string[start_index:end_index]]

    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # Return the 4th smallest ASCII value
    return sorted_ascii_values[3]
