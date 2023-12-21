
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 14 and 66 (inclusive)
    indices = []
    for i, char in enumerate(string):
        if 14 <= i <= 66:
            indices.append(i)
    # Get the ASCII values of the characters at those indices

    ascii_values = [ord(string[index]) for index in indices]
    # Sort the ASCII values in ascending order

    sorted_ascii_values = sorted(ascii_values)
    # Return the 8th smallest ASCII value

    return sorted_ascii_values[7]
