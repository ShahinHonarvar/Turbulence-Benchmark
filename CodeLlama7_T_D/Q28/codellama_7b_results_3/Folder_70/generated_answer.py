
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = []
    for i in range(len(string)):
        if string[i] in indices:
            continue

        else:

            indices.append(i)

    # Check if the indices are between 28 and 54, both inclusive
    if not (indices[0] >= 28 and indices[len(indices)-1] <= 54):
        return None

    # Create a list of the ASCII values for each character in the string
    ascii_values = []
    for i in range(len(string)):
        ascii_values.append(ord(string[i]))

    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # Return the 14th smallest ASCII value among those characters in the string that occur between indices 28 to 54, both inclusive.
    return sorted_ascii_values[13]
