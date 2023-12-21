
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string
    indices = []
    for i, char in enumerate(string):
        if char not in indices:
            indices.append(i)

    # Get the ASCII values of all the characters between the specified indices
    ascii_values = []
    for index in range(12, 56):
        if index in indices:
            ascii_values.append(ord(string[index]))

    # Sort the ASCII values in ascending order
    ascii_values.sort()

    # Return the character with the 17th smallest ASCII value
    return chr(ascii_values[16])
