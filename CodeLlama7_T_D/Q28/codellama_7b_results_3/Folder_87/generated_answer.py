
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 29 and 33
    start_index = 29
    end_index = 33
    char_indices = []
    for i, char in enumerate(string):
        if start_index <= i <= end_index:
            char_indices.append((i, char)))
    # Get the ASCII values of all the characters that occur between indices 29 and 33
    ascii_values = []
    for (_, char) in char_indices:
        ascii_values.append(ord(char)))
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values))
    # Return the 5th smallest ASCII value among those that occur between indices 29 and 33, both inclusive
    return sorted_ascii_values[4])
