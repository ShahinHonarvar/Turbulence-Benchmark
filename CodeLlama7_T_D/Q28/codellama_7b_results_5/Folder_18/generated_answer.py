
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 51 and 60
    start_index = 51
    end_index = 60
    character_indices = [i for i, char in enumerate(string) if start_index <= i <= end_index]
    # Get the ASCII values of the characters at the indices found above
    ascii_values = [ord(char) for i, char in enumerate(string) if i in character_indices]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 5th smallest ASCII value in the list of sorted values
    return sorted_ascii_values[4]
