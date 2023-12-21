
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = []
    for i, char in enumerate(string):
        if char not in indices:
            indices.append(i)

    # Check if the desired index is within the range of indices
    if 51 <= len(indices) and len(indices) <= 89:

        # Get the ASCII values of the characters at the desired indices
        ascii_values = []
        for i in indices[50:90]:
            ascii_values.append(ord(string[i]))

        # Sort the ASCII values in ascending order
        sorted_ascii_values = sorted(ascii_values)

        # Return the 14th smallest ASCII value
        return sorted_ascii_values[13]

    else:

        # If the desired index is not within the range of indices, return an error message
